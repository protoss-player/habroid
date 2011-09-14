# coding: utf-8

import json

import tornado.web
from pyquery import PyQuery

BLOG_LIST = 'http://habrahabr.ru/bloglist/'

class BlogTypes(tornado.web.RequestHandler):
    """ Gets the blog types list
    """
    
    def get(self):
        d = PyQuery(url=BLOG_LIST)
        
        data = []
        blog_id = None
        for tag in d(".side-rubrikator li").children():
            if blog_id is None:
                blog_id = tag.attrib['href'].replace(BLOG_LIST, '')
                blog_name = tag.text.encode('utf-8')
            else:
                data.append({'id': blog_id.encode('utf-8'), 'name': blog_name, 'count': int(tag.text[1:-1])})
                blog_id = None

        jsonp = self.get_argument('callback')
        self.set_header('Content-Type', 'text/javascript')
        self.write(''.join([jsonp, '(', json.dumps({'response': data}), ')']))
