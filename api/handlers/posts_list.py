# coding: utf-8

import json

import tornado.web
from pyquery import PyQuery

class PostsList(tornado.web.RequestHandler):
    """ Gets the list of posts in the spicific blog.
    """
    
    def get(self):
        try:
            blog_id = '/'.join(['blogs', self.get_argument('blog')])
        except:
            blog_id = ''
            
        print blog_id
            
        url = 'http://habrahabr.ru/{}'.format(blog_id)
        d = PyQuery(url=url)
        
        data = []
        for tag in d("#main-content a.topic"):
            link = tag.attrib['href']
            data.append({'link': link, 'title': tag.text})
            
        jsonp = self.get_argument('callback')
        self.set_header('Content-Type', 'text/javascript')
        self.write(''.join([jsonp, '(', json.dumps({'response': data}), ')']))
