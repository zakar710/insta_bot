from instabot import Bot
import my_config
import random

bot = Bot()
bot.login(username = my_config.USERNAME,password = my_config.PASSWORD)

# bot.upload_photo("yoda.jpg",caption="cute biscuits available")
# following aspecific person
bot.follow("rt_business")
# send amessage to someone
# bot.send_message("Hi from baby",['rt_business'])

# followers = bot.get_user_followers("runtime2021")
# for follower in followers:
#     print(bot.get_user_info(follower))
