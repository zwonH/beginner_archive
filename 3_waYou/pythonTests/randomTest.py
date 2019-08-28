import random
import secrets

address = "https://www.instagram.com/explore/tags/"
hashtag_list = ["travel", "India", "korea", "seoul"]
hashtag = random.choice(hashtag_list)
print (hashtag)
url = address + hashtag
print (url)

address = "https://www.instagram.com/explore/tags/"
hashtag_list = ["travel", "India", "korea", "seoul"]
hashtag = secrets.choice(hashtag_list)
print (hashtag)
url = address + hashtag
print (url)