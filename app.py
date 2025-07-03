import os
import json
import logging
from flask import Flask, request, jsonify
from slack_sdk.signature import SignatureVerifier
from dotenv import load_dotenv

# For local development, load .env file
if os.environ.get("FLASK_ENV") != "production": # A simple check to not load in prod
    load_dotenv()

from config import Config
from handlers import event_handlers, interaction_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config) # Load configuration

signature_verifier = SignatureVerifier(Config.SLACK_SIGNING_SECRET)

@app.before_request
def verify_slack_signature():
    """Verify incoming Slack requests."""
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        logger.warning("Invalid Slack signature detected!")
        return "Invalid signature", 403

@app.route("/slack/events", methods=["POST"])
def slack_events():
    """Handle Slack Events API requests (team_join, reaction_added)."""
    payload = request.json
    
    # Handle URL verification challenge
    if "challenge" in payload:
        logger.info("Received Slack URL verification challenge.")
        return jsonify({"challenge": payload["challenge"]})

    event_type = payload["event"]["type"]
    logger.info(f"Received Slack event of type: {event_type}")

    if event_type == "team_join":
        event_handlers.handle_team_join(payload["event"])
    elif event_type == "reaction_added":
        event_handlers.handle_reaction_added(payload["event"])
    
    return "", 200 # Acknowledge receipt

@app.route("/slack/interactive", methods=["POST"])
def slack_interactive():
    """Handle Slack Interactive API requests (button clicks)."""
    payload = json.loads(request.form["payload"])
    
    action_id = payload["actions"][0]["action_id"]
    logger.info(f"Received interactive payload, action_id: {action_id}")

    # Delegate to appropriate handler based on action_id or block_id
    if action_id.startswith("select_cohort_"):
        interaction_handlers.handle_cohort_selection(payload)
    # Add more conditions for other interactive actions if needed
    
    return "", 200 # Acknowledge receipt

if __name__ == "__main__":
    logger.info("Starting Flask app locally...")
    app.run(debug=True, host="0.0.0.0", port=Config.PORT)