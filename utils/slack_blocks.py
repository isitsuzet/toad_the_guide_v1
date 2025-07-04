from config import Config

def get_welcome_and_cohort_blocks(user_id, channel_ids_map):
    """Returns Slack Block Kit for the welcome and cohort selection message."""
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🎉 *Welcome to the community, <@{user_id}>!* 🎉\n"
                        "I'm your friendly guide, Toad. I'm here to help you get started and connected."
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*1️⃣ Tell us about your study year:*"
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
                    "text": "*(Alternatively, react with: :one: for 2021, :two: for 2022, :three: for 2023, :four: for 2024, :five: for 2025)*"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]

def get_notification_preference_blocks():
    """Returns Slack Block Kit for the notification preference message."""
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*2️⃣ How would you like to be notified?*"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: for *ALL* notifications\n"
                            ":bell: for *ONLY IMPORTANT* announcements\n"
                            ":no_bell: for *NO NOTIFICATIONS* (you'll mute channels manually)"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]

# New functions for each of the final messages
def get_channel_browser_blocks():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*3️⃣ Explore more channels:*\n"
                        "Find and join channels that interest you: <slack://channel_browser>"
            }
        },
        {
            "type": "divider"
        }
    ]

def get_profile_editing_blocks():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*4️⃣ Complete your profile:*\n"
                        "Help your peers get to know you! <slack://profile>"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*(For more details on editing your profile, check the Slack docs: <https://slack.com/help/articles/204092246-Edit-your-profile>)*"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]

def get_introduction_blocks():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                f"text": "*5️⃣ Introduce yourself!* 👋\n"
                        f"Pop into the <#{Config.CHANNEL_IDS['mess_intros']}> channel and say hello to the community!"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "That's it for now! Enjoy your time in the community! 🥳"
            }
        }
    ]

def get_post_onboarding_customize_blocks():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🎉 *You've now set up the basic structure of your Slack workspace!* 🎉\n\n"
                        "If you want to customize your experience further, please choose the 'Customize' button below."
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Customize"
                    },
                    "style": "primary", # Make it stand out
                    "value": "customize_start",
                    "action_id": "customize_start"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]

def get_mandatory_classes_blocks():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Do you want to join the channels for the mandatory classes of your semester?*"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "If yes, please choose your current semester below:"
                }
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "Semester 1" },
                    "value": "1",
                    "action_id": "select_semester_1"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "Semester 2" },
                    "value": "2",
                    "action_id": "select_semester_2"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "Semester 3" },
                    "value": "3",
                    "action_id": "select_semester_3"
                },
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "Semester 4" },
                    "value": "4",
                    "action_id": "select_semester_4"
                }
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": { "type": "plain_text", "text": "I want to manually choose channels" },
                    "value": "manual",
                    "action_id": "manual_channels_choice" # New action ID for manual selection
                }
            ]
        },
        {
            "type": "divider"
        }
    ]


def get_social_channels_blocks():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*This space is a great opportunity to get in touch with your peers.*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                f"text": "If you want to join the social channels, please select 'Social' below. "
                         f"In <#{Config.CHANNEL_IDS['social_channel']}>, you can plan casual meetups and have academic unrelated talks with your peers."
            },
            "accessory": {
                "type": "button",
                "text": { "type": "plain_text", "text": "Join Social Channel" },
                "value": "social_channel_join", # Value doesn't matter much for a single channel
                "action_id": "join_social_channel"
            }
        },
        {
            "type": "divider"
        }
    ]
