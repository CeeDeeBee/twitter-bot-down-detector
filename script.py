import tweepy
from datetime import datetime, timedelta
import requests

auth = tweepy.OAuthHandler(Consumer Key, Consumer Secret)
auth.set_access_token(Access Token, Access Token Secret)

api = tweepy.API(auth)

def getTweet(acc, hours, days):
	tweet = api.user_timeline(id = acc, count = 1)[0]

	time = tweet.created_at
	print(datetime.utcnow().time())
	print(time.time())

	elapsed = datetime.utcnow() - time
	print(elapsed)

	if hours > 0:
		timeType = "hour(s)"
		timeValue = hours
	else:
		timeType = "day(s)"
		timeValue = days

	if elapsed > timedelta(hours = hours, days = days):
		print(tweet.created_at)
		r = requests.post("https://maker.ifttt.com/trigger/script_trigger/with/key/" + webhookKey, data = {"value1": acc, "value2": timeValue, "value3": timeType})
		print(r.status_code, r.reason)
	else:
		print("Less than {} {} since last tweet".format(timeValue, timeType))

getTweet("TrumpGone", 0, 1)
getTweet("TrumpGone2", 0, 1)
getTweet("POTUSApproval", 0, 2)
getTweet("BTCtoUSD_", 2, 0)
getTweet("ETHtoUSD", 2, 0)
getTweet("LTCtoUSD", 2, 0)