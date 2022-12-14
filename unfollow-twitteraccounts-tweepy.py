import tweepy
from cred import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)


def unfollower():

    followers = api.get_follower_ids(screen_name=api.verify_credentials().screen_name)
    friends = api.get_friend_ids(screen_name=api.verify_credentials().screen_name)
    print("You follow:", len(friends))    
    
    for friend in friends[::-1]:
        if friend not in followers:
            api.destroy_friendship(user_id = friend)
        else:
            pass
        
    friends = api.friends_ids(screen_name=api.me().screen_name)
    print("Now you're following:", len(friends))

unfollower()