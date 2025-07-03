import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import Config

logger = logging.getLogger(__name__)

# Initialize Slack WebClient once
slack_client = WebClient(token=Config.SLACK_BOT_TOKEN)

def send_dm_message(user_id, text, blocks=None):
    """Sends a direct message to a user."""
    try:
        slack_client.chat_postMessage(
            channel=user_id,
            text=text,
            blocks=blocks
        )
        logger.info(f"DM sent to {user_id}")
    except SlackApiError as e:
        logger.error(f"Error sending DM to {user_id}: {e}")

def invite_user_to_channel(user_id, channel_id):
    """Invites a user to a specified channel."""
    try:
        slack_client.conversations_invite(
            channel=channel_id,
            users=[user_id]
        )
        logger.info(f"User {user_id} invited to channel {channel_id}")
    except SlackApiError as e:
        if e.response["error"] == "already_in_channel":
            logger.warning(f"User {user_id} already in channel {channel_id}")
        elif e.response["error"] == "not_in_channel":
            logger.error(f"Bot not in channel {channel_id}. Please invite the bot to this channel.")
        else:
            logger.error(f"Error inviting user {user_id} to channel {channel_id}: {e}")

# Add other Slack API interaction functions here if needed
