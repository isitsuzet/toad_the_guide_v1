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
from handlers import event_handlers, interaction_handlers, command_handlers

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

@app.route("/slack/interactive", methods=["POST"])
def slack_interactive():
    payload = json.loads(request.form["payload"])
    action_id = payload["actions"][0]["action_id"]
    logger.info(f"Received interactive payload, action_id: {action_id}")

    if action_id.startswith("select_cohort_"):
        interaction_handlers.handle_cohort_selection(payload)
    # --- NEW: Route customize button ---
    elif action_id == "customize_start":
        interaction_handlers.handle_customize_start(payload)
    # --- NEW: Route semester selection buttons (will be added soon) ---
    elif action_id.startswith("select_semester_"):
        interaction_handlers.handle_semester_selection(payload)
    # --- NEW: Route social channel button (will be added soon) ---
    elif action_id == "join_social_channel":
        interaction_handlers.handle_join_social_channel(payload)
    elif action_id == "manual_channels_choice":
        interaction_handlers.handle_manual_channels_choice(payload)
    
    return "", 200

@app.route("/slack/command", methods=["POST"])
def slack_command():
    # Slack slash commands use application/x-www-form-urlencoded, not JSON
    command_data = request.form
    logger.info(f"Received slash command: {command_data['command']} from {command_data['user_id']}")
    
    if command_data['command'] == "/init_introduction":
        command_handlers.handle_init_introduction_command(command_data)
        # Slash commands need an immediate response within 3 seconds,
        # otherwise Slack shows "response_url took too long".
        # We can send a quick acknowledgement.
        return jsonify({"text": "Sending introduction guide to your DMs..."})
    
    return jsonify({"text": "Unknown command"}), 400

if __name__ == "__main__":
    logger.info("Starting Flask app locally...")
    app.run(debug=True, host="0.0.0.0", port=Config.PORT)
