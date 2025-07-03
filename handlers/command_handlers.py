import logging
from services import user_onboarding
from services import slack_service # Might be useful for sending ephemeral messages

logger = logging.getLogger(__name__)

def handle_init_introduction_command(command_data):
    """Handles the /init_introduction slash command."""
    user_id = command_data["user_id"]
    response_url = command_data["response_url"] # Used for delayed/ephemeral messages

    logger.info(f"Handling /init_introduction command for user: {user_id}")

    # Call the existing onboarding function to send the final messages
    user_onboarding.send_introduction_guide(user_id)

    # Optionally, you could send a delayed message to the channel where the command was issued
    # For instance, a private message visible only to the user who issued the command:
    # slack_service.send_ephemeral_message(
    #     channel_id=command_data["channel_id"],
    #     user_id=user_id,
    #     text="I've sent the introduction guide to your direct messages."
    # )
