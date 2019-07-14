# #it's a bot...but for slack!
# import slack
# import ssl as ssl_lib
# import certifi
# from config import secret_token


# def notify_advisor(web_client: slack.WebClient, user_id: str, channel: str):
#     # Get the onboarding message payload
#     message = "AYY LMAO"

#     # Post the onboarding message in Slack
#     response = web_client.chat_postMessage(message)

# # ============== Message Events ============= #
# # When a user sends a DM, the event type will be 'message'.
# # Here we'll link the update_share callback to the 'message' event.
# @slack.RTMClient.run_on(event="message")
# def message(**payload):
#     """Display the onboarding welcome message after receiving a message
#     that contains "start".
#     """
#     data = payload["data"]
#     web_client = payload["web_client"]
#     channel_id = data.get("channel")
#     user_id = data.get("user")
#     text = data.get("text")

#     if text and text.lower() == "start":
#         return notify_advisor(web_client, user_id, channel_id)

# if __name__ == "__main__":
#     ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
#     slack_token = secret_token
#     rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
#     rtm_client.start()