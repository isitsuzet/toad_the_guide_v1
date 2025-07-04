from config import Config

def get_home_tab_view(user_id):
    """
    Generates the Block Kit view for the App Home tab.
    This is a static view, but can be made dynamic based on user_id if needed.
    """
    return {
        "type": "home",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "👋 Welcome to Toad the Guide!",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "I'm here to help you navigate your community space and get connected."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Quick Actions:*"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Start Onboarding Guide"
                        },
                        "style": "primary",
                        "value": "start_onboarding_from_home",
                        "action_id": "start_onboarding_from_home"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Customize Channels"
                        },
                        "value": "start_customize_from_home",
                        "action_id": "start_customize_from_home"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Browse All Channels"
                        },
                        "url": "slack://channel_browser"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Edit My Profile"
                        },
                        "url": "slack://profile"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": f"Go to #intros"
                        },
                        "url": f"slack://channel?team={Config.SLACK_TEAM_ID}&id={Config.CHANNEL_IDS['mess_intros']}" # Requires team ID
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "💡 _Your personal space with Toad the Guide._"
                    }
                ]
            }
        ]
    }
