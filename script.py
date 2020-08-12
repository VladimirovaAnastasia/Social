import os
from pathlib import Path
from dotenv import load_dotenv
import requests
import argparse
import telegram
import vk_api

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def create_parser():
    parser = argparse.ArgumentParser(description='Post img and text in vk, fb and tg')
    parser.add_argument('post_img', help='The image for the post')
    parser.add_argument('post_text', help='The text for the post')

    return parser


def post_telegram(post_img, post_text):
    TG_TOKEN = os.getenv("TG_TOKEN")
    TG_CHAT_ID = os.getenv("TG_CHAT_ID")

    bot = telegram.Bot(token=TG_TOKEN)
    bot.send_photo(chat_id=TG_CHAT_ID, photo=open(post_img, 'rb'))
    bot.send_message(chat_id=TG_CHAT_ID, text=post_text)


def post_facebook(post_img, post_text):
    FB_TOKEN = os.getenv("FB_TOKEN")
    FB_GROUP_ID = os.getenv("FB_GROUP_ID")

    files = {'upload_file': open(post_img, 'rb')}
    url = 'https://graph.facebook.com/' + str(FB_GROUP_ID) + '/photos'
    data = {
        "access_token": FB_TOKEN,
        "caption": post_text}
    requests.post(url, files=files, data=data)


def post_vkontakte(post_img, post_text):
    VK_LOGIN = os.getenv("VK_LOGIN")
    VK_TOKEN = os.getenv("VK_TOKEN")
    vk_session = vk_api.VkApi(login=VK_LOGIN, token=VK_TOKEN)

    try:
        vk_session._auth_token()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)

    VK_ALBUM_ID = os.getenv("VK_ALBUM_ID")
    VK_GROUP_ID = os.getenv("VK_GROUP_ID")
    photo = upload.photo(
        post_img,
        album_id=VK_ALBUM_ID,
        group_id=VK_GROUP_ID
    )
    media_id = photo[0]['id']

    vk3 = vk_session.get_api()
    vk3.wall.post(owner_id='-' + VK_GROUP_ID,
                  message=post_text,
                  attachments='photo-' + str(VK_GROUP_ID) + '_' + str(media_id))


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    post_img = args.post_img
    post_text = args.post_text

    post_telegram(post_img, post_text)
    post_facebook(post_img, post_text)
    post_vkontakte(post_img, post_text)