from instabot import Bot
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../'))
args = {i.split(":")[0]: i.split(":")[1]
        for i in open("pw.config", "r").read().strip().split("\n")}


bot = Bot(
    filter_private_users=False,
    filter_users_without_profile_photo=False,
    max_follows_per_day=1000,
    min_media_count_to_follow=0,
    follow_delay=3
)  # Play around with these settings
bot.login(username=args['username'], password=args['password'])

for username in eval(args['users']):
    bot.follow_followers(username)
