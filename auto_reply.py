import praw
import pdb
import re
import os
#from praw.helpers import comment_stream
 
reddit = praw.Reddit("stormBot")
#r.login()
 
target_text = "stormlight"
response_text = "I love Stormlight! Great to see a fellow fan"
 
processed = []
while True:
    for c in reddit.subreddit('fantasy').stream.comments():
        if target_text in c.body and c.id not in processed:
            c.reply(response_text)
            print('responded to ' + target_text)
            processed.append(c.id)
