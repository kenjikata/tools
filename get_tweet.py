# -*- coding: utf-8 -*-
# 2014.7.22

import twitter
import socket
import urllib
 
class TwitterSearch:
    def __init__(self):
        self._lang = 'ja'
        self._api = twitter.Api(
            consumer_key = ‘######’,
            consumer_secret = '######',
            access_token_key = '######',
            access_token_secret = '######'
        )
 
    def search(self, word, page=1):
        #search_word = word     # NG
        search_word = urllib.quote(word.encode('utf-8'))    # OK
        #result = self._api.GetSearch(term=search_word, page=page, lang=self._lang)
        result = self._api.GetSearch(term=search_word, count=1000, lang=self._lang)
        for status in result:
            print status.text
            print '-' * 30
 
if __name__ == '__main__':
    word = u’話題’
    t = TwitterSearch()
    t.search(word)
