import os

class Config:
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
    PORT = int(os.environ.get("PORT", 8080))
    SLACK_TEAM_ID = os.environ.get("SLACK_TEAM_ID")

    # --- Channel IDs (retrieved from environment variables) ---
    CHANNEL_IDS = {
        "cohort_2021": os.environ.get("CHANNEL_ID_2021"),
        "cohort_2022": os.environ.get("CHANNEL_ID_2022"),
        "cohort_2023": os.environ.get("CHANNEL_ID_2023"),
        "cohort_2024": os.environ.get("CHANNEL_ID_2024"),
        "cohort_2025": os.environ.get("CHANNEL_ID_2025"),
        "official_announcements": os.environ.get("CHANNEL_ID_ANNOUNCEMENTS"),
        "mess_intros": os.environ.get("CHANNEL_ID_INTRODUCTIONS"),
        "social_channel": os.environ.get("CHANNEL_ID_SOCIAL"),
        "S1_Entrepreneurship": os.environ.get("CHANNEL_ID_S1_ENTREPRENEURSHIP"),
        "S1_Micro": os.environ.get("CHANNEL_ID_S1_MICRO"),
        "S1_EconBusinessNature": os.environ.get("CHANNEL_ID_S1_ECONBUSINESSNATURE"),
        "S1_IntroStatistics": os.environ.get("CHANNEL_ID_S1_INTROSTATISTICS"),
        "S1_EconClimateChange": os.environ.get("CHANNEL_ID_S1_ECONCLIMATECHANGE"),

        "S2_IntroPsychology": os.environ.get("CHANNEL_ID_S2_INTROPSYCHOLOGY"),
        "S2_Macro": os.environ.get("CHANNEL_ID_S2_MACRO"),
        "S2_DemographySocialInequality": os.environ.get("CHANNEL_ID_S2_DEMOGRAPHYSOCIALINEQUALITY"),
        "S2_EconInequality": os.environ.get("CHANNEL_ID_S2_ECONINEQUALITY"),
        "S2_DataAnalysisEconometrics": os.environ.get("CHANNEL_ID_S2_DATAANALYSISECONOMETRICS"),

        "S3_ManagingDS": os.environ.get("CHANNEL_ID_S3_MANAGINGDS"),
        "S3_EconDesign": os.environ.get("CHANNEL_ID_S3_ECONDESIGN"),
        "S3_DigitalTransformation": os.environ.get("CHANNEL_ID_S3_DIGITALTRANSFORMATION"),
        "S3_FinanceAccounting": os.environ.get("CHANNEL_ID_S3_FINANCEACCOUNTING"),
        "S3_DataScience": os.environ.get("CHANNEL_ID_S3_DATASCIENCE"),

        "S4_Ethics": os.environ.get("CHANNEL_ID_S4_ETHICS"),
        "S4_PublicPolicy": os.environ.get("CHANNEL_ID_S4_PUBLICPOLICY"),
        "S4_DigitalTransformationChangeMgt": os.environ.get("CHANNEL_ID_S4_DIGITALTRANSFORMATIONCHANGEMGT"),
    
    }

    
    
    # Validate that essential channel IDs are set (optional but good practice)
    for key, value in CHANNEL_IDS.items():
        if value is None:
            raise ValueError(f"Missing required environment variable for channel ID: {key}. Please set it.")


    MANDATORY_SEMESTER_CHANNELS = {
        "1": ["S1_Entrepreneurship", "S1_Micro", "S1_EconBusinessNature", "S1_IntroStatistics", "S1_EconClimateChange"],
        "2": ["S2_IntroPsychology", "S2_Macro", "S2_DemographySocialInequality", "S2_EconInequality", "S2_DataAnalysisEconometrics"],
        "3": ["S3_ManagingDS", "S3_EconDesign", "S3_DigitalTransformation", "S3_FinanceAccounting", "S3_DataScience"],
        "4": ["S4_Ethics", "S4_PublicPolicy", "S4_DigitalTransformationChangeMgt"]
    }
    
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


    # Validate that essential config values are set (optional but good practice)
    if SLACK_BOT_TOKEN is None or SLACK_SIGNING_SECRET is None or SLACK_TEAM_ID is None:
        raise ValueError("Missing essential Slack API environment variables (SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, SLACK_TEAM_ID).")
    for key, value in CHANNEL_IDS.items():
        if value is None:
            raise ValueError(f"Missing required environment variable for channel ID: {key.upper()}. Please set it.")


