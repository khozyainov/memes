import requests
import json
import reddit
import vk_api

# Токен бессрочный с правами wall, market и photos


TOKEN = "6e2b71a6d0862ba01904e5c9dee5e1ce15199ef4b997f05458481931a8d25839aa4c9eaad5064f4356595"
GROUP_ID = "173009640"
OWNER_ID_GROUP = "-173009640"
API_V = "5.87"

def main():

    login, password = 'entonyj@yandex.ru', 'a95nton412'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)   
    photos = reddit.get_photos_from_reddit('memes')
    upload.photo_wall(photos, group_id=GROUP_ID)

if __name__ == '__main__':
    main()