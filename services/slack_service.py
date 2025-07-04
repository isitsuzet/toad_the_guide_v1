import logging
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import Config

logger = logging.getLogger(__name__)

# Initialize Slack WebClient once
slack_client = WebClient(token=Config.SLACK_BOT_TOKEN)

def send_dm_message(user_id, text, blocks=None):
    """Sends a direct message to a user."""
    # Ensure text is not empty if blocks are present.
    # Slack recommends always providing a text fallback for blocks.
    if blocks and not text:
        text = "Message from your bot (please update your client to see full content)" # Provide a fallback text
    
    try:
        slack_client.chat_postMessage(
            channel=user_id,
            text=text, # Always send text
            blocks=blocks
        )
        logger.info(f"DM sent to {user_id}")
    except SlackApiError as e:
        logger.error(f"Error sending DM to {user_id}: {e}")

def invite_user_to_channel(user_id, channel_id):
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

def send_ephemeral_message(channel_id, user_id, text):
    """Sends a temporary message visible only to the specified user in a channel."""
    try:
        slack_client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            text=text
        )
        logger.info(f"Ephemeral message sent to {user_id} in {channel_id}")
    except SlackApiError as e:
        logger.error(f"Error sending ephemeral message to {user_id} in {channel_id}: {e}")


def send_delayed_message(user_id, text_message, delay_seconds, blocks=None):
    """Sends a message to a user after a specified delay."""
    time.sleep(delay_seconds)
    # Ensure the text_message is passed correctly to send_dm_message
    send_dm_message(user_id, text_message, blocks)
    logger.info(f"Delayed message sent to {user_id} after {delay_seconds} seconds.")

def publish_home_tab(user_id, view_blocks):
    """Publishes a Block Kit view to a user's App Home tab."""
    try:
        slack_client.views_publish(
            user_id=user_id,
            view=view_blocks
        )
        logger.info(f"Home tab published for user {user_id}")
    except SlackApiError as e:
        logger.error(f"Error publishing Home tab for user {user_id}: {e}")
