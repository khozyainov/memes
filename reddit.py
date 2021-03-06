import praw
import urllib.request
import io

CLIENT_ID = '3bPZJic_DrwV0A'
CLIEN_SECRET = 'RY41rFo97fNKRktGEsI894enFEw'
USER_AGENT = 'khozyainov_service'

def get_photos_from_reddit(subreddit, count):
    reddit = praw.Reddit(client_id=CLIENT_ID,
                        client_secret=CLIEN_SECRET,
                        user_agent=USER_AGENT)

    subreddit = reddit.subreddit(subreddit)
    new_posts = subreddit.top(time_filter='day', limit=count+10)

    posts = []
    post = {'title': '', 'photo': '', 'score': ''}

    for submission in new_posts:
        url = submission.url
        file_name = url.rsplit('/',1)[1]
        file_format = None
        if '.' in file_name:
            file_format = file_name.rsplit('.',1)[1]
        if (file_format != 'jpg' and file_format != 'png'):
            continue
        destination = '/tmp/' + file_name
        urllib.request.urlretrieve(url, destination)
        post = {'title': submission.title, 'photo': file_name, 'score': submission.score}
        posts.append(post)
        if (len(posts) == count):
            break

    return posts