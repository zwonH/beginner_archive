import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 해시태그 랜덤으로 선택하여 주소 생성
address = "https://www.instagram.com/explore/tags/"
hashtag_list = ["travel", "desert", "amazon", "ocean"]
hashtag = random.choice(hashtag_list)

url = address + hashtag

# for selenium...
DRIVER_DIR = "/Applications/chromedriver"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(5)
driver.get(url)
elem = driver.find_elements_by_tag_name("body")

# 이미지 링크 9개가 담길 리스트
img_list = []

pagedowns = 1

while pagedowns < 3:
    elem[0].send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    img = driver.find_elements_by_css_selector('.EZdmt .KL4Bh img')
    for i in img:
       img_list.append(i.get_attribute('src'))
    pagedowns += 1

img_list = list(set(img_list))

# 9개의 링크 중 하나를 선택하여 img_link로!
# 이제 이 링크만 html과 잘 연결하면 됨
img_link = random.choice(img_list)
print(img_link)

driver.close()