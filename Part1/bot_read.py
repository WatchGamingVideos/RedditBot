#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("memes")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
