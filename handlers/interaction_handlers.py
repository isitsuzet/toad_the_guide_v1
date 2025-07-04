import logging
from services import user_onboarding
from config import Config

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
