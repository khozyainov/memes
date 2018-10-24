import praw
import urllib.request
import io

CLIENT_ID = '3bPZJic_DrwV0A'
CLIEN_SECRET = 'RY41rFo97fNKRktGEsI894enFEw'
USER_AGENT = 'khozyainov_service'

def get_photos_from_reddit(subreddit):
    reddit = praw.Reddit(client_id=CLIENT_ID,
                        client_secret=CLIEN_SECRET,
                        user_agent=USER_AGENT)

    subreddit = reddit.subreddit(subreddit)
    new_posts = subreddit.new(limit=3)
    photos = []

    for submission in new_posts:
        url = submission.url
        file_format = url.rsplit('.',1)[1]
        if (file_format != 'jpg' and file_format != 'jpeg'):
            continue
        with urllib.request.urlopen(url) as resource:
            photo = io.BytesIO(resource.read())
            photos.append(photo)
        if (len(photos) == 24):
            break

    return photos