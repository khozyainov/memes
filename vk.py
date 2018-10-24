import requests
import json
import reddit
import vk_requests
import time

GROUP_ID = "173009640"
APP_ID = "6730383"

LOGIN = 'entonyj@yandex.ru'
PASSWORD = 'a95nton412'


def main():

    print("start")
    api = vk_requests.create_api(app_id=APP_ID, login=LOGIN, password=PASSWORD, scope='wall,photos')

    posts = reddit.get_photos_from_reddit('memes', 24)
    print("downloaded {count} posts".format(count=len(posts)))
    current_time = int(time.time())
    publish_time = current_time + 60
    
    for post in posts:
        photo = 'tmp/'+post['photo']

        upload_url = api.photos.getWallUploadServer(group_id=GROUP_ID)['upload_url']
        request = requests.post(upload_url, files={'photo': open(photo, "rb")})
        
        
        params = {
                'server': request.json()['server'],
                'photo': request.json()['photo'],
                'hash': request.json()['hash'],
                'group_id': GROUP_ID
                }

        save_r = api.photos.saveWallPhoto(**params)
        
        photo_id = save_r[0]['id']
        owner_id = save_r[0]['owner_id'] 

        params = {'attachments': 'photo{owner_id}_{photo_id}'.format(owner_id=owner_id, photo_id=photo_id),
                'message': post['title'],
                'owner_id': '-' + GROUP_ID,
                'from_group': '1',
                'publish_date': publish_time,
                }
        api.wall.post(**params)
        print("published {title}".format(title=post['title']))
        publish_time = publish_time + 60 * 60
        time.sleep(1)
    print("success")

if __name__ == '__main__':
    main()