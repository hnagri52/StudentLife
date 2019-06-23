import time
import json
import requests
# access token
token = "ADD_YOUR_TOKEN_HERE"


def saveToFile(name, content):
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)


def readFile(name):
    with open(name, "r") as f:
        content = f.read().encode('ascii', 'ignore')
        return content.decode("utf-8")


def getMsgs():
    print("Getting Messages")
    # this function get all the messages from the slack team-search channel
    # it will only get all the messages from the team-search channel
    fname_msg = "msg.json"
    while True:
        channelsURL = "https://slack.com/api/conversations.list?token=" + token
        channels = json.loads(requests.get(
            channelsURL).content.decode("utf-8"))["channels"]
        team_search_id = [channel["id"]
                          for channel in channels if channel["name"] == "team-search"]
        slack_url = "https://slack.com/api/conversations.history?token=" + \
            token + "&channel=" + team_search_id[0]
        channel_msgs = requests.get(slack_url).content.decode("utf-8")
        # Saving the msgs to local msg.json file
        saveToFile(fname_msg, channel_msgs.encode('ascii', 'ignore').decode("utf-8"))
        channel_msg = json.loads(readFile(fname_msg))["messages"]
        # making data safe to use for printing - there are some msgs that have unsafe characters that will stop the program
        for i in channel_msg[::-1]:
            i["text"] = i["text"].encode("ascii", "ignore")
        # these msgs are ready to be processed
        return channel_msg


def getUsers():
    print("Getting Users")
    # this function get a list of users in workplace including bots 
    users = []
    fname_user = "users.json"
    channelsURL = "https://slack.com/api/users.list?token=" + token + "&pretty=1"
    members = json.loads(requests.get(
        channelsURL).content.decode("utf-8"))["members"]
    # generating new json
    for member in members:
        if ("email") in member["profile"]:
            valid_member = {}
            valid_member["id"] =  member["id"]
            valid_member["name"] = member["profile"]["real_name"]
            valid_member["email"] = member["profile"]["email"]
            users.append(valid_member)
    saveToFile(fname_user, json.dumps({"users": users}))
    return {"users": users}  # lsit of all users


def main():
    # getting user and messages from team-search every 5 minutes
    print("Slack Team-Seach Scrapper")
    getUsers()
    getMsgs()
    time.sleep(300)

main()