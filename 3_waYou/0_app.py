from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.waYou

import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



@app.route('/')
def home():
    return '와유'

@app.route('/wayou')
def main():
    return render_template('wayou.html')


@app.route('/post', methods=['POST'])
def post():
    comment_receive = request.form['comment_give']

    comment = {'comment': comment_receive}
    db.comments.insert_one(comment)
    print(comment)
    return jsonify({'result': 'success'})


@app.route('/post', methods=['GET'])
def get():
    dansangs = db.comments.find({}, {'_id': 0})
    return jsonify({'result': 'success', 'comments': list(dansangs)})

@app.route('/img', methods=['GET'])
def getImgLink():
    # 해시태그 랜덤으로 선택하여 주소 생성
    address = "https://www.instagram.com/explore/tags/"
    hashtag_list = ["travel", "desert", "ocean", "europe", "beach", "landscape", "hawaii", "eiffeltower", "honolulu", "wonderlust", "italy", "natgeotravel", "citybestpics", "worldplaces", "best_worldplaces", "wonderful_places", "beautifuldestinations", "bestvacation", "visiteurope", "europetrip", "indianphotography", "world", "worldphotography", "nature", "naturephotography", "naturelovers", "himalayas", "humanendeavour", "traveling", "beautifulview", "travelphotography", "explore", "thegreatoutdoors", "travellingthroightheworld", "discoverearth", "modernoutdoors", "ournaturedays", "moodygrams", "earthfocus"]
    hashtag = random.choice(hashtag_list)

    url = address + hashtag

    # for selenium...
    DRIVER_DIR = "/Applications/chromedriver"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(DRIVER_DIR, chrome_options=options)
    driver.implicitly_wait(5)
    driver.get(url)
    elem = driver.find_elements_by_tag_name("body")


    # 이미지 링크 9개가 담길 리스트
    img_list = []

    pagedowns = 1

    while pagedowns < 2:
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
    return(img_link)
    print (img_link)

    driver.close()


if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)