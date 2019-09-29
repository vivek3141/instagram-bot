from instabot import Bot
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../'))
args = {i.split(":")[0]: i.split(":")[1]
        for i in open("pw.config", "r").read().strip().split("\n")}
bot = Bot(
    filter_private_users=False,
    filter_users_without_profile_photo=False,
    max_follows_per_day=10000,
    min_media_count_to_follow=0,
    follow_delay=0,
    unfollow_delay=0,
)
bot.login(username=args['username'], password=args['password'])

followers = bot.followers
following = bot.following
print(len(following))
print(len(followers))


for i in following:
    if not i in followers:
        if i in args['exceptions']:
            continue
        bot.unfollow(i)
