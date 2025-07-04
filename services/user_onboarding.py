import logging
import threading
import time


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
    send_final_onboarding_messages_step_by_step(user_id)

def send_final_onboarding_messages_step_by_step(user_id):
    """Sends the concluding messages of the onboarding, one by one."""
    # Message 1: Channel browser
    slack_service.send_dm_message(user_id, "Explore Channels", slack_blocks.get_channel_browser_blocks())
    time.sleep(1)
    
    # Message 2: Profile editing
    slack_service.send_dm_message(user_id, "Update Your Profile", slack_blocks.get_profile_editing_blocks())
    time.sleep(1)

    # Message 3: Self-introduction
    slack_service.send_dm_message(user_id, "Say Hello!", slack_blocks.get_introduction_blocks())

    # Message 4: Send the post-onboarding customization prompt

    customize_blocks = slack_blocks.get_post_onboarding_customize_blocks()
    slack_service.send_dm_message(user_id, "Ready for more?", customize_blocks)


# Function to handle the customization flow 
def start_customization_flow(user_id):
    """Starts the customization flow after the basic onboarding."""
    logger.info(f"Starting customization flow for {user_id}")
    
    # 1. Mandatory Classes Prompt
    mandatory_class_blocks = slack_blocks.get_mandatory_classes_blocks()
    slack_service.send_dm_message(user_id, "Choose your mandatory classes:", mandatory_class_blocks)

# We will use this later for the delayed message
def _send_delayed_module_prompt(user_id):
    """Helper function to send the module prompt after a delay."""
    time.sleep(5) # The actual 5-second delay
    slack_service.send_dm_message(
        user_id,
        "If you want to join channels for modules you have this semester, please type `/set_my_classes`"
    )
    logger.info(f"Delayed module prompt sent to {user_id}")


def send_introduction_guide(user_id):
    """Sends the introduction guide messages to a user (reusing final onboarding messages)."""
    logger.info(f"Sending introduction guide to {user_id}")
    # Call the new step-by-step function
    slack_service.send_dm_message(user_id, "Here's your introduction guide:") # Optional intro message
    send_final_onboarding_messages_step_by_step(user_id)

def start_customization_flow(user_id):
    """Starts the customization flow after the basic onboarding."""
    logger.info(f"Starting customization flow for {user_id}")
    mandatory_class_blocks = slack_blocks.get_mandatory_classes_blocks()
    slack_service.send_dm_message(user_id, "Choose your mandatory classes:", mandatory_class_blocks)

def proceed_to_events_jobs_channels(user_id):
    """Sends the events/jobs channel prompt."""
    events_jobs_blocks = slack_blocks.get_events_jobs_channels_blocks()
    slack_service.send_dm_message(user_id, "More Opportunities:", events_jobs_blocks)


def proceed_to_social_channels(user_id):
    """Proceeds to the social channels prompt."""
    social_blocks = slack_blocks.get_social_channels_blocks()
    slack_service.send_dm_message(user_id, "Connect Socially:", social_blocks)
    
    # Trigger the delayed module prompt after this
    threading.Thread(target=slack_service.send_delayed_message, args=(user_id, "If you want to join channels for modules you have this semester, please type `/set_my_classes`", 5)).start()

