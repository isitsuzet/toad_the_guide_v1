import logging
from services import user_onboarding
from config import Config
from services import slack_service
import threading

logger = logging.getLogger(__name__)

def handle_cohort_selection(payload):
    """Handles button clicks for cohort selection."""
    user_id = payload["user"]["id"]
    value = payload["actions"][0]["value"] # This will be the channel ID from the button

    logger.info(f"Handling cohort selection button click from {user_id} with value: {value}")
    
    # The value of the button is already the channel ID, so no need for further lookup
    user_onboarding.handle_cohort_choice(user_id, value)

def handle_customize_start(payload):
    """Handles the 'Customize' button click."""
    user_id = payload["user"]["id"]
    logger.info(f"User {user_id} clicked 'Customize'.")
    user_onboarding.start_customization_flow(user_id)

def handle_semester_selection(payload):
    user_id = payload["user"]["id"]
    semester = payload["actions"][0]["value"] # This will be "1", "2", "3", or "4"
    logger.info(f"User {user_id} selected Semester {semester}.")

    if semester in Config.MANDATORY_SEMESTER_CHANNELS:
        channels_to_join_keys = Config.MANDATORY_SEMESTER_CHANNELS[semester]
        
        joined_channels_names = []
        for channel_key in channels_to_join_keys:
            channel_id = Config.CHANNEL_IDS.get(channel_key)
            if channel_id:
                slack_service.invite_user_to_channel(user_id, channel_id)
                joined_channels_names.append(f"<#{channel_id}>")
            else:
                logger.warning(f"Channel ID for key '{channel_key}' not found in config.")
        
        if joined_channels_names:
            slack_service.send_dm_message(user_id, f"You've been invited to the mandatory channels for Semester {semester}: {', '.join(joined_channels_names)}.")
        else:
            slack_service.send_dm_message(user_id, f"No mandatory channels found for Semester {semester}. Please check bot configuration.")
    else:
        slack_service.send_dm_message(user_id, "Invalid semester selection.")
    
    # After semester selection (or manual choice), proceed to social channels
    user_onboarding.proceed_to_social_channels(user_id)

def handle_manual_channels_choice(payload):
    user_id = payload["user"]["id"]
    logger.info(f"User {user_id} chose to manually select channels.")
    slack_service.send_dm_message(user_id, "No problem! You can browse and join channels manually anytime using the channel browser (link in your introduction guide).")
    
    # After manual choice, proceed to social channels
    user_onboarding.proceed_to_social_channels(user_id)
