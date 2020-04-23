import tweepy
import numpy as np
import re
import json
from wordcloud_fa import WordCloudFa
from os import path
from PIL import Image
from math import ceil

class PersianWordCloud:

    def __init__(self, username, numberOfTweets, backGround):

        self.username = username
        self.numberOfTweets = numberOfTweets
        self.backGround = backGround

        with open('/home/mohammad/PycharmProjects/Persian Word Cloud Twitter/config.json', 'r') as f:
            dev = json.load(f)

        dev = dev['twitter']
        consKey = dev['consKey'] 
        consSecret = dev['consSecret'] 
        accessKey = dev['accessKey']
        accessSecret = dev['accessSecret']
        self.d = path.dirname(__file__)
        auth = tweepy.OAuthHandler(consumer_key=consKey, consumer_secret=consSecret)
        auth.set_access_token(accessKey, accessSecret)
        self.api = tweepy.API(auth)

    def execute(self):

        numberOfPages = 1
        numberOfTweetsPerPage = 200

        counter = 0
        cloud = ""
        txt = ""

        if self.numberOfTweets > 200:
            numberOfPages = ceil(self.numberOfTweets/200)
        else:
            numberOfTweetsPerPage = self.numberOfTweets
        for i in range(numberOfPages):
            tweets = self.api.user_timeline(screen_name=self.username, count=numberOfTweetsPerPage, page=i)
            for each in tweets:
                cloud = each.text
                cloud = re.sub(r'[A-Za-z@_]*', '', cloud)
                counter += 1
                txt = txt + ' ' + each.text

        txt = re.sub(r'[A-Za-z@]*', '', txt)

        twitter_mask = np.array(Image.open(path.join(self.d, "templates/cloud/twitter-logo.jpg")))

        stop = ['می', 'من', 'که', 'به', 'رو', 'از', 'ولی', 'با', 'یه', 'این', 'نمی',
                'هم', 'شد', 'ها', 'اما', 'تو', 'واقعا', 'در', 'نه', 'دارم', 'باید',
                'آره', 'برای', 'تا', 'چه', 'کنم', 'بود', 'همه', 'دیگه', 'ای', 'اون',
                'تی', 'حالا', 'بی', 'د', 'چرا', 'بابا', 'منم', 'کیه', 'توی', 'نیست', 'چی', 'باشه', 'که',
                'بودم', 'می کنم', 'که', 'اینه', 'بهتر', 'داره', 'اینه', 'که',
                'کردن', 'می', 'کن', 'بعد', 'دیگه', '', '', '', '']



        wc = WordCloudFa(
            # font_path='IranNastaliq.ttf',
            persian_normalize=True,
            max_words=1000,
            margin=0,
            width=3000,
            height=2500,
            min_font_size=1,
            max_font_size=1000,
            background_color=self.backGround,
            mask=twitter_mask,
            include_numbers=False,
            collocations=False

        )

        wc.add_stop_words(stop)
        wc.generate(txt)

        directory = 'static/images/' + self.username + '.png'
        directory = path.join(self.d, directory)
        image = wc.to_image()
        image.save(directory)
