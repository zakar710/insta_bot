from instapy import InstaPy
from instapy import smart_run
import schedule
import time


# account credentials
my_username  = 'runtime2021'
my_password = 'turashashe'

# def job():

    # logging into instagram account
session = InstaPy(username=my_username,
                        password=my_password,
                        headless_browser = False)


with smart_run(session):
    
    # check for those accounts with many followers that are likely not to follow you back
    session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=5000,
                                        min_followers=10,
                                        min_following=10)

    session.set_do_follow(True,percentage=100)

    # session.set_dont_like(['nsfw','kia','ford'])

    # session.follow_by_tags(['tanzania','daressalaam','serengeti'],amount=10) 

    # session.follow_by_locations(['216731354/dar-es-salaam-tanzania/'],amount=5) 

        # session.like_by_locations(['216731354/dar-es-salaam-tanzania/'],amount=10)                                
popeye_followers = session.grab_followers(username="melian_software", amount="full", live_match=True, store_locally=True)
##now, `popeye_followers` variable which is a list- holds the `Followers` data of "Popeye" at requested time
#  
    # schedule.every().day.at("6:00").do(job)
    # schedule.every().day.at("18:00").do(job)

    # while True:
    #     schedule.run_panding()
    #     time.sleep(10)