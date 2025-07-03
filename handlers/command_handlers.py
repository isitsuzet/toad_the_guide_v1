import logging
from services import user_onboarding
from services import slack_service # Might be useful for sending ephemeral messages

logger = logging.getLogger(__name__)

def handle_init_introduction_command(command_data):
    """Handles the /init_introduction slash command."""
    user_id = command_data["user_id"]
    # response_url = command_data["response_url"] # You can use this for ephemeral responses if needed

    logger.info(f"Handling /init_introduction command for user: {user_id}")

    # Call the function that starts the full onboarding flow
    user_onboarding.start_onboarding_flow(user_id)

    # Send a quick acknowledgement back to the user in the channel where they typed the command
    # This is important for slash commands to not show "response_url took too long"
    # You can customize this message.
    slack_service.send_ephemeral_message(
        channel_id=command_data["channel_id"],
        user_id=user_id,
        text="Starting your introduction guide in your Direct Messages! Please check your DMs with Toad."
    )
