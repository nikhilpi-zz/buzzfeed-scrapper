# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from firebase import firebase
import json


class BuzzlinksPipeline(object):
  def process_item(self, item, spider): 
    d = {}   
    d['article_title'] = str(item['article_title'])
    d['link'] = str(item['link'])
    d['current_url'] = str(item['current_url'])
    d['referring_url'] = str(item['referring_url'])
    d['link_domain'] = str(item['link_domain'])
    d['depth'] = item['depth']
    fb = firebase.FirebaseApplication('https://torid-fire-7900.firebaseio.com', None)
    result = fb.post('/buzzfeedLinks', d)
    return item
