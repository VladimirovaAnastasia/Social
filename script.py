import os
from dotenv import load_dotenv
import requests
import argparse
import telegram
import vk_api
from urllib.parse import urljoin

load_dotenv()


def create_parser():
    parser = argparse.ArgumentParser(description='Post img and text in vk, fb and tg')
    parser.add_argument('post_img', help='The image for the post')
    parser.add_argument('post_text', help='The text for the post')

    return parser


def post_telegram(tg_token, tg_chat_id, post_img, post_text):
    with open(post_img, 'rb') as post_img:
        bot = telegram.Bot(token=tg_token)
        bot.send_photo(chat_id=tg_chat_id, photo=post_img)
        bot.send_message(chat_id=tg_chat_id, text=post_text)


def post_facebook(fb_token, fb_group_id, post_img, post_text):
    with open(post_img, 'rb') as post_img:
        files = {'upload_file': post_img}
        url = urljoin('https://graph.facebook.com/', fb_group_id, '/photos')
        data = {
            "access_token": fb_token,
            "caption": post_text}
        response = requests.post(url, files=files, data=data)
        decoded_response = response.json()
        if 'error' in decoded_response:
            raise requests.exceptions.HTTPError(decoded_response['error'])


def post_vkontakte(vk_login, vk_token, vk_album_id, vk_group_id, post_img, post_text):
    vk_session = vk_api.VkApi(login=vk_login, token=vk_token)
    vk_session._auth_token()

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        post_img,
        album_id=vk_album_id,
        group_id=vk_group_id
    )
    media_id = photo[0]['id']

    vk = vk_session.get_api()
    vk.wall.post(owner_id=f"-{vk_group_id}",
                         message=post_text,
                         attachments=f"photo-{vk_group_id}_{media_id}")


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    post_img = args.post_img
    post_text = args.post_text

    TG_TOKEN = os.getenv("TG_TOKEN")
    TG_CHAT_ID = os.getenv("TG_CHAT_ID")
    FB_TOKEN = os.getenv("FB_TOKEN")
    FB_GROUP_ID = os.getenv("FB_GROUP_ID")
    VK_LOGIN = os.getenv("VK_LOGIN")
    VK_TOKEN = os.getenv("VK_TOKEN")
    VK_ALBUM_ID = os.getenv("VK_ALBUM_ID")
    VK_GROUP_ID = os.getenv("VK_GROUP_ID")

    post_telegram(TG_TOKEN, TG_CHAT_ID, post_img, post_text)
    post_facebook(FB_TOKEN, FB_GROUP_ID, post_img, post_text)
    post_vkontakte(VK_LOGIN, VK_TOKEN, VK_ALBUM_ID, VK_GROUP_ID, post_img, post_text)
