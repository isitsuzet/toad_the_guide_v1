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

def send_final_onboarding_messages(user_id):
    """Sends the concluding messages of the onboarding."""
    slack_service.send_dm_message(user_id, "Browse and join more channels here: <slack://channel_browser>")
    slack_service.send_dm_message(user_id, "To help your peers get to know you, please take a moment to fill out your Slack profile: <https://slack.com/help/articles/204092246-Edit-your-profile>")
    
    introduction_channel_id = Config.CHANNEL_IDS["mess_intros"]
    slack_service.send_dm_message(user_id, f"Lastly, we'd love for you to give a short introduction about yourself in the <#{introduction_channel_id}> channel! Say hello and tell us a bit about you.")

# --- New Function for Manual Introduction Guide Trigger ---
def send_introduction_guide(user_id):
    """Sends the introduction guide messages to a user."""
    logger.info(f"Sending introduction guide to {user_id}")
    slack_service.send_dm_message(user_id, "Here's your introduction guide:")
    send_final_onboarding_messages(user_id) # Reuse the existing messages
