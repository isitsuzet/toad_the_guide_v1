import logging
from services import user_onboarding
from services import slack_service
from utils.views import home_tab_view
from config import Config

logger = logging.getLogger(__name__)

def handle_team_join(event):
    """Handles the 'team_join' event when a new user joins the workspace."""
    user_id = event["user"]["id"]
    logger.info(f"Handling team_join event for user: {user_id}")
    user_onboarding.start_onboarding_flow(user_id)

def handle_reaction_added(event):
    """Handles the 'reaction_added' event for emoji responses."""
    user_id = event["user"]
    reaction = event["reaction"]
    item_ts = event["item"]["ts"]
    item_channel = event["item"]["channel"] # The DM channel with the bot

    logger.info(f"Reaction '{reaction}' added by {user_id} on message {item_ts} in channel {item_channel}")

    # Check if the reaction is for cohort selection (emoji alternative)
    if reaction in Config.EMOJI_COHORTS:
        cohort_key = Config.EMOJI_COHORTS[reaction]
        cohort_channel_id = Config.CHANNEL_IDS[cohort_key]
        user_onboarding.handle_cohort_choice(user_id, cohort_channel_id)
    
    # Check if the reaction is for notification preference
    elif reaction in Config.EMOJI_NOTIFICATIONS:
        preference = Config.EMOJI_NOTIFICATIONS[reaction]
        user_onboarding.handle_notification_choice(user_id, preference)
    else:
        logger.info(f"Ignored unknown reaction '{reaction}'")

def handle_app_home_opened(event):
    user_id = event["user"]
    logger.info(f"App Home opened by user: {user_id}")

    # Add this log to confirm the view generation is attempted
    logger.info(f"Attempting to generate Home tab view for user {user_id}")
    home_view = home_tab_view.get_home_tab_view(user_id)
    
    # Add this log to confirm the publish call is attempted
    logger.info(f"Attempting to publish Home tab for user {user_id}")
    slack_service.publish_home_tab(user_id, home_view)
    logger.info(f"publish_home_tab function call completed for user {user_id}") # Confirm call finishes

