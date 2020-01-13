import tweepy
import re

# Initial setup
consumer_key=""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

incidents = []
# Iterate though all of the tweets from northants fire
for x, tweet in enumerate(tweepy.Cursor(api.user_timeline, id="northantsfire", include_entities=True).items()):
    # init
    text = tweet.text.upper()
    incident_type = []

    # Can't use the time from this as they aren't posted in real time
    date = str(tweet.created_at)[:10]
    # The time is always in the form XX:YY
    time = re.findall("[0-9][0-9][:][0-9][0-9]", text)
    # Find word with #s in (They always do #Location)
    location = re.findall("#\S+", text)
    source = tweet.entities["urls"]

    if not time:
        # Not tweeting about an incident
        continue

    if "FALSE ALARM" in text or "False" in text:
        incident_type.append("False")
    if "EMASNHSTRUST" in text:
        incident_type.append("Ambulance")
    if "RTC" in text or "VEHICLE" in text or "CAR" in text:
        incident_type.append("Car")
    if "CONTROLLED" in text:
        incident_type.append("Controlled")
    if "EMAS_CFR" in text:
        incident_type.append("CRT")
    if "NORTHANTSPOLICE" in text:
        incident_type.append("Police")
    if "FIRE" in text or "SMOKE" in text:
        incident_type.append("Fire")

    incidents.append([date, time, incident_type, location, source])

    if x == 30:
        break
for incident in incidents:
    print(incident)