import os

class Config:
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
    PORT = int(os.environ.get("PORT", 8080))

    # --- Channel IDs (retrieved from environment variables) ---
    CHANNEL_IDS = {
        "cohort_2021": os.environ.get("CHANNEL_ID_2021"),
        "cohort_2022": os.environ.get("CHANNEL_ID_2022"),
        "cohort_2023": os.environ.get("CHANNEL_ID_2023"),
        "cohort_2024": os.environ.get("CHANNEL_ID_2024"),
        "cohort_2025": os.environ.get("CHANNEL_ID_2025"),
        "official_announcements": os.environ.get("CHANNEL_ID_ANNOUNCEMENTS"),
        "mess_intros": os.environ.get("CHANNEL_ID_INTRODUCTIONS"),
    }
    
    # Validate that essential channel IDs are set (optional but good practice)
    for key, value in CHANNEL_IDS.items():
        if value is None:
            raise ValueError(f"Missing required environment variable for channel ID: {key}. Please set it.")


    # Emoji mappings for reactions (these are static, so they can stay here)
    EMOJI_COHORTS = {
        "one": "cohort_2021",
        "two": "cohort_2022",
        "three": "cohort_2023",
        "four": "cohort_2024",
        "five": "cohort_2025"
    }

    EMOJI_NOTIFICATIONS = {
        "white_check_mark": "ALL",
        "bell": "IMPORTANT",
        "no_bell": "NONE"
    }