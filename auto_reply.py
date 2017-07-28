import praw
import config
#import pdb
#import re
#import os

#from praw.helpers import comment_stream
def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Mist_Bot v 0.1")
	return r

def run_bot(r):
	processed = []
	for comment in r.subreddit("fantasy").comments(limit = 25):
		if "mistborn" in comment.body and comment.id not in processed:
			comment.reply("Mistborn is great! Hope to see a video game soon")
			print ("Responded to comment" + comment.id)
			processed.append(comment.id)

r = bot_login()

while True:
	run_bot(r)

 
#target_text = "stormlight"
#response_text = "I love Stormlight! Great to see a fellow fan"
 
#processed = []
#while True:
#    for c in reddit.subreddit('fantasy').stream.comments():
#        if target_text in c.body and c.id not in processed:
#            c.reply(response_text)
#            print('responded to ' + target_text)
#            processed.append(c.id)
