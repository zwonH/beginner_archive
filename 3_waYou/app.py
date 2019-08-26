from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.waYou

import requests
from bs4 import BeautifulSoup


@app.route('/')
def home():
    return '와유'

@app.route('/main')
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


if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)