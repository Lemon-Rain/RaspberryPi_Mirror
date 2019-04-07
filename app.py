# -*- coding:utf-8 -*-

from flask import Flask, render_template, json
import feedparser
import urllib
import re

app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('index.html')


@app.route('/news')
def get_news():
    news_list = []
    page = urllib.urlopen('http://www.ftchinese.com/rss/news')
    new_xml = page.read()
    feed = feedparser.parse(new_xml)
    for e in feed.entries:
        news_list.append(re.findall(r'.*<p>(.*)</p>.*', e.description.encode('utf8'))[0])

    return json.dumps(news_list)


if __name__ == '__main__':
    app.run()
