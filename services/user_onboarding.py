import logging
from services import slack_service
from utils import slack_blocks
from config import Config

logger = logging.getLogger(__name__)

def start_onboarding_flow(user_id):
    """Initiates the onboarding flow for a new user."""
    logger.info(f"Starting onboarding flow for {user_id}")
    
    cohort_selection_blocks = slack_blocks.get_welcome_and_cohort_blocks(user_id, Config.CHANNEL_IDS)
    slack_service.send_dm_message(user_id, "Welcome! Please select your study year.", cohort_selection_blocks)

def handle_cohort_choice(user_id, cohort_channel_id):
    """Handles the user's cohort selection and proceeds to notification prefs."""
    slack_service.invite_user_to_channel(user_id, cohort_channel_id)
    slack_service.send_dm_message(user_id, f"Great! You've been invited to <#{cohort_channel_id}>.")
    
    notification_blocks = slack_blocks.get_notification_preference_blocks()
    slack_service.send_dm_message(user_id, "Please choose your notification preference.", notification_blocks)

def handle_notification_choice(user_id, preference):
    """Handles notification preference and sends follow-up messages."""
    if preference == "ALL":
        slack_service.send_dm_message(
            user_id,
            "You've selected ALL notifications. Your channels will notify you as usual. "
            "Remember, you can always adjust notification settings for individual channels manually."
        )
    elif preference == "IMPORTANT":
        announcements_channel_id = Config.CHANNEL_IDS["official_announcements"]
        slack_service.invite_user_to_channel(user_id, announcements_channel_id)
        slack_service.send_dm_message(
            user_id,
            f"You've selected ONLY IMPORTANT notifications. You've been invited to <#{announcements_channel_id}>. "
            "For other channels, please consider muting them manually. Click a channel name > 'Notifications' > 'Mute channel'."
        )
    elif preference == "NONE":
        slack_service.send_dm_message(
            user_id,
            "You've selected NO notifications. Please remember to mute channels you join. "
            "Click a channel name > 'Notifications' > 'Mute channel'."
        )
    
    # Send the final onboarding messages after notification choice
    send_final_onboarding_messages(user_id)

def send_final_onboarding_messages_step_by_step(user_id):
    """Sends the concluding messages of the onboarding, one by one."""
    # Message 1: Channel browser
    slack_service.send_dm_message(user_id, "Explore Channels", slack_blocks.get_channel_browser_blocks())

    # Message 2: Profile editing
    slack_service.send_dm_message(user_id, "Update Your Profile", slack_blocks.get_profile_editing_blocks())

    # Message 3: Self-introduction
    slack_service.send_dm_message(user_id, "Say Hello!", slack_blocks.get_introduction_blocks())


def send_introduction_guide(user_id):
    """Sends the introduction guide messages to a user (reusing final onboarding messages)."""
    logger.info(f"Sending introduction guide to {user_id}")
    # Call the new step-by-step function
    slack_service.send_dm_message(user_id, "Here's your introduction guide:") # Optional intro message
    send_final_onboarding_messages_step_by_step(user_id)
