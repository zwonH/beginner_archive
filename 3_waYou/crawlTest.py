import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.instagram.com/explore/tags/travel/"



DRIVER_DIR = '/Applications/chromedriver'

driver = webdriver.Chrome(DRIVER_DIR)

driver.implicitly_wait(5)
driver.get(url)

elem = driver.find_elements_by_tag_name("body")
# print(elem);

alt_list = []

pagedowns = 1

while pagedowns < 5:
    elem[0].send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    img = driver.find_elements_by_css_selector('div.KL4Bh > img')
    # print(img)
    for i in img:
        alt_list.append(i.get_attribute('src'))
    pagedowns += 1

alt_list = list(set(alt_list))

print(alt_list)


driver.close()