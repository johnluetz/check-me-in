import time
import os
import re
from random import randrange
from config import secret_token
from slackclient import SlackClient

# Constant Variables
# instantiate Slack client
slack_client = SlackClient(secret_token)
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
        notify_advisor(" ", " ", " ", " ")

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

def notify_advisor(advisorname, stu_name, stu_major, stu_time):
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"] #logs into bot
    
    channel='CL2L8BF34' #channel ID for #check-in-updates
    advisors = {'John':'@UL917897E', 'Audry':'@ULE3F8PAL', 'Sreenidhi':'@UL2MA3ZL3', 'Matthew':'@ULG7W4FHU', 'Rachel':'@ULG8X0WAJ', 'Brittany':'@UL2MCFNQJ',
                'Jackie':'@UL2P7LDCJ', 'Faith':'@UL2PCV9QS', 'Kaleigh':'@ULGTE0HFZ', 'Ericka':'@UL3KMRH42', 'Shreya':'@UL3L38NR1', 'Christina':'@UL8MNF1K3'} #list of advisors and ID
    #@'s an advisor to let em know who showed up
    message = slack_client.api_call(
    'chat.postMessage',
    link_names=1,
    channel='#check-in-updates',
    text="<"+advisors[advisorname]+'> Your '+stu_time+', '+stu_name+' of major '+stu_major+' is here!'
    )#end api-call


#if __name__ == "__main__":
def start_bot(self):
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")