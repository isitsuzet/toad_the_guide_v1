from config import Config # To access CHANNEL_IDS if needed for dynamic block generation

def get_welcome_and_cohort_blocks(user_id, channel_ids_map):
    """Returns Slack Block Kit for the welcome and cohort selection message."""
    # You can customize these blocks significantly
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🎉 Welcome to the community, <@{user_id}>! I'm your friendly guide, Toad! I'm here to help you get started."
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "To help us get you connected with the right people, please tell us which year you started studying:"
            }
        },
        {
            "type": "actions",
            "block_id": "cohort_selection",
            "elements": [
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "2021" },
                    "value": channel_ids_map["cohort_2021"],
                    "action_id": "select_cohort_2021"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "2022" },
                    "value": channel_ids_map["cohort_2022"],
                    "action_id": "select_cohort_2022"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "2023" },
                    "value": channel_ids_map["cohort_2023"],
                    "action_id": "select_cohort_2023"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "2024" },
                    "value": channel_ids_map["cohort_2024"],
                    "action_id": "select_cohort_2024"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "2025" },
                    "value": channel_ids_map["cohort_2025"],
                    "action_id": "select_cohort_2025"
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*(Alternatively, you can react with: :one: for 2021, :two: for 2022, :three: for 2023, :four: for 2024, :five: for 2025)*"
                }
            ]
        }
    ]

def get_notification_preference_blocks():
    """Returns Slack Block Kit for the notification preference message."""
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "How would you like to be notified in the channels you join? Please react to indicate your preference:"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: for ALL, :bell: for ONLY IMPORTANT, :no_bell: for NO NOTIFICATION"
                }
            ]
        }
    ]
