import praw
import config
import time
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
	for comment in r.subreddit("fantasy").comments(limit = 5):
		if "e" in comment.body and comment.id not in processed:
			#comment.reply("Mistborn is great!")
			#print ("Responded to comment" + comment.id)
			processed.append(comment.id)
			print(processed[len(processed) - 1].body)

r = bot_login()

while True:
	try:
		run_bot(r)
	except:
		time.sleep(10)
 
#target_text = "stormlight"
#response_text = "I love Stormlight! Great to see a fellow fan"
 
#processed = []
#while True:
#    for c in reddit.subreddit('fantasy').stream.comments():
#        if target_text in c.body and c.id not in processed:
#            c.reply(response_text)
#            print('responded to ' + target_text)
#            processed.append(c.id)
