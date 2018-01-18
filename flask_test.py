from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route('/')
def default():
        return """
        <h1>RSS FEEDER!</h1>
        <a href="/bbc">bbc</a>
        <a href="/cnn">cnn</a>
        <a href="/fox">fox</a>
        <a href="/iol">iol</a>
        """

@app.route('/bbc')
def get_bbcnews():
        headline = 'BBC'
        feed = feedparser.parse(RSS_FEEDS['bbc'])
        return render_template('home.html', articles=feed['entries'],headline=headline)

@app.route('/cnn')
def get_cnnnews():
        headline = 'CNN'
        feed = feedparser.parse(RSS_FEEDS['cnn'])
        return render_template('home.html', articles=feed['entries'],headline=headline)

@app.route('/fox')
def get_foxnews():
        headline = 'FOX'
        feed = feedparser.parse(RSS_FEEDS['fox'])
        return render_template('home.html', articles=feed['entries'],headline=headline)

@app.route('/iol')
def get_iolnews():
        headline = 'IOL'
        feed = feedparser.parse(RSS_FEEDS['iol'])
        return render_template('home.html', articles=feed['entries'],headline=headline)

app.run(port=5000, debug=True)