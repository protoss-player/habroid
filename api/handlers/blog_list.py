# coding: utf-8

import json

import tornado.web
from pyquery import PyQuery

BLOG_LIST = 'http://habrahabr.ru/bloglist/'
BLOGS = 'http://habrahabr.ru/blogs/'

class BlogList(tornado.web.RequestHandler):
    """ Gets the list of blogs in the selected category
    """
    
    def get(self):
        try:
            cat_id = self.get_argument('cat')
        except:
            cat_id = ''

        d = PyQuery(url='{}/{}'.format(BLOG_LIST, cat_id))
        
        data = []
        for tag in d("a.title"):
            blog_id = tag.attrib['href'].replace(BLOGS, '')
            data.append({'id': blog_id, 'name': tag.text})
            
        jsonp = self.get_argument('callback')
        self.set_header('Content-Type', 'text/javascript')
        self.write(''.join([jsonp, '(', json.dumps({'response': data}), ')']))
