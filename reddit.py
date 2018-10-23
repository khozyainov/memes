import praw
import urllib.request
import ssl

reddit = praw.Reddit(client_id='3bPZJic_DrwV0A',
                     client_secret='RY41rFo97fNKRktGEsI894enFEw',
                     user_agent='khozyainov_service')

subreddit = reddit.subreddit('memes')

memes = subreddit.new(limit=3)
context = ssl._create_unverified_context()

for submission in memes:
    url = submission.url
    destination = url.rsplit('/',1)[1]
    urllib.request.urlretrieve(url, destination)