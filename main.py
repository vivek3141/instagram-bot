from instabot import Bot
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../'))


bot = Bot(filter_private_users=False, filter_users_without_profile_photo=False,
          max_follows_per_day=1000, min_media_count_to_follow=0, follow_delay=3) # Play around with these settings
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

for username in args.users:
    bot.follow_followers(username)
