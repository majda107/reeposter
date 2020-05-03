from instabot import Bot
from time import sleep
from random import random
from random import choice
import math

# USER NAMES YOU'LL STEAL USERS THAT BOT WILL FOLLOW FROM
sucker_sources = [
    # 'sucward',`
    'zucctheberg',
    'zuccctheberg',
    'zucktheberg'
    # 'sucwardmeme'
]

ig_username = "your username"
ig_password = "your password"

bot = Bot(max_likes_to_like=100000000, min_likes_to_like=0,
          like_delay=2, follow_delay=2)


def login():
    print(" ~ ~ ~ ~ ~ Loggin in")
    bot.login(username=ig_username, password=ig_password)


def logout():
    print(" ~ ~ ~ ~ ~ Logging out")
    bot.logout()


def bot_sleep():
    sleep_time = (random() * 2) * (60 * 60)
    print(f" ~ ~ ~ ~ ~ Sleeping for {sleep_time} seconds")
    sleep(sleep_time)


def get_latest_media(source):
    user_id = bot.get_user_id_from_username(source)
    media = bot.get_user_medias(user_id)[0]
    return media


def get_to_like():
    return math.ceil((random() * 30) + 50)


def get_cut_likers(media):
    likers = bot.get_media_likers(media)
    to_like = min(len(likers), get_to_like())
    likers = likers[0:to_like]
    return likers


def download_latest_video(source):
    user_id = bot.get_user_id_from_username(source)
    medias = bot.get_user_medias(user_id)

    for media in medias:
        bot.api.media_info(media)
        json = bot.api.last_json
        # print(json)
        media_type = json["items"][0]["media_type"]
        if media_type == 2:
            print(" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ FOUND VIDEO!!!!!!!")
            bot.download_video(media, folder="videos")
            return


while True:
    source = choice(sucker_sources)
    login()

    # download_latest_video(source)
    # bot.upload_video("thot.MP4", "Doe this girl lit :#")
    # bot.upload_photo("meme.jpg", "Doe that's lit")

    media = get_latest_media(source)
    likers = get_cut_likers(media)

    for liker in likers:
        bot.follow_users([liker])
        sleep(random() * 5 + 1)

    logout()
    bot_sleep()
