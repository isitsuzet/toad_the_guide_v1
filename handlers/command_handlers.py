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


def handle_set_my_classes_command(command_data):
    """Handles the /set_my_classes slash command."""
    user_id = command_data["user_id"]
    logger.info(f"Handling /set_my_classes command for user: {user_id}")

    # Send initial message for module selection
    intro_blocks = slack_blocks.get_module_selection_intro_blocks()
    slack_service.send_dm_message(user_id, "Module Selection", intro_blocks)

    # Send modules for each semester
    for semester_name, modules_dict in Config.MODULES_BY_SEMESTER.items():
        if modules_dict: # Only send if there are modules for this semester
            module_blocks = slack_blocks.get_module_selection_blocks(semester_name, modules_dict)
            slack_service.send_dm_message(user_id, f"Modules for {semester_name}", module_blocks)
            # Add a small delay between semester blocks for better UX
            slack_service.send_delayed_message(user_id, "", 0.5) # 0.5 seconds delay without text

    # Send final message
    outro_blocks = slack_blocks.get_module_selection_outro_blocks()
    slack_service.send_dm_message(user_id, "Module Selection Complete!", outro_blocks)

    # Send a quick ephemeral response to avoid Slack timeout
    slack_service.send_ephemeral_message(
        channel_id=command_data["channel_id"],
        user_id=user_id,
        text="Module selection options have been sent to your DMs!"
    )
