import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('stormBot')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Creates an empty list of the posts that have already been replied to (in this case none) when the program is run
if not os.path.isfile("replied_to_posts.txt"):
    replied_to_posts = []

# Give out a list of the posts that have already been replied to
else:
    # Change the file into a list and remove any empty values
    with open("replied_to_posts.txt", "r") as f:
        replied_to_posts = f.read()
        replied_to_posts = replied_to_posts.split("\n")
        replied_to_posts = list(filter(None, replied_to_posts))

# Get the top 15 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=15):
    print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in replied_to_posts:

        # Do a case insensitive search
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Love Stormlight, always good to see another fan!")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            replied_to_posts.append(submission.id)

# Write our updated list back to the file
with open("replied_to_posts.txt", "w") as f:
    for post_id in replied_to_posts:
        f.write(post_id + "\n")
