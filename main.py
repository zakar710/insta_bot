from instabot import Bot
import my_config
import random
import time


bot = Bot()
bot.login(username = my_config.USERNAME,password = my_config.PASSWORD)

follows_limit = 30

# bot.upload_photo("yoda.jpg",caption="cute biscuits available")

# send amessage to someone
# bot.send_message("Hi from baby",['rt_business'])

i = 0
followers = bot.get_user_followers("melian_software")

for follower in followers:
    
    # print(bot.get_user_info(follower))
    if(i <= follows_limit):

            try:
            # following aspecific person
                bot.follow(follower)
                print("followed"+i)
                time.sleep(random.randint(5,10))

            except:
                print("error")
                time.sleep(random.randint(100,300))

            i +=1
