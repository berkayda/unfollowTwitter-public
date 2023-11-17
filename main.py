import tweepy
import time
from datetime import datetime
import pytz
import os
import random

istanbul_timezone = pytz.timezone("Europe/Istanbul")

consumer_key = "WRITEYOURS"
consumer_secret = "WRITEYOURS"
access_token = "WRITE-YOURS"
access_token_secret = "WRITEYOURS"

# Kullanıcı adını atayın
user = "WRITEUSERNAME"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Following list
following = []
for friend in tweepy.Cursor(api.get_friends, screen_name=user).items():
    time.sleep(4)
    following.append(friend)

    now = datetime.utcnow()
    now = now.replace(tzinfo=pytz.utc)  
    time_of_calculation = now.astimezone(istanbul_timezone).strftime("%d-%m-%Y %H:%M:%S TSİ")
    print("Following list creating... "+ time_of_calculation)

# Takip edilen kullanıcı adlarını txt dosyasına yazın
with open('following.txt', 'w') as f:
    for user in following:
        f.write(user.screen_name + '\n')


# Followers list
followers = []
for follower in tweepy.Cursor(api.get_followers, screen_name=user).items():
    time.sleep(4)
    followers.append(follower)

    now = datetime.utcnow()
    now = now.replace(tzinfo=pytz.utc)
    time_of_calculation = now.astimezone(istanbul_timezone).strftime("%d-%m-%Y %H:%M:%S TSİ")
    print("Followers list creating... "+ time_of_calculation)

with open('followers.txt', 'w') as f:
    for user in followers:
        f.write(user.screen_name + '\n')


with open("following.txt", "r") as f1:
    following_usernames = f1.read().splitlines()

with open("followers.txt", "r") as f2:
    followers_usernames = f2.read().splitlines()

to_unfollow = []
for username in following_usernames:
    if username not in followers_usernames and username not in ["elonmusk", "financialjuice"]:
        to_unfollow.append(username)
print(to_unfollow)
print(f"To unfollow:: {len(to_unfollow)}")


unfollowed_count = 0
for username in to_unfollow:
    wait_time = random.randint(20, 50)
    time.sleep(wait_time)

    user = api.get_user(screen_name=username)
    api.destroy_friendship(user_id=user.id)
    print(username + " unfollowed")
    unfollowed_count += 1
print("Total {} account unfollowed.".format(unfollowed_count))


os.remove("following.txt")
print("following.txt deleted.")
os.remove("followers.txt")
print("followers.txt deleted.")
