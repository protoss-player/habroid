# coding: utf-8

import tornado.web

class BlogTypes(tornado.web.RequestHandler):
    """ Gets the blog types list
    """
    
    def get(self):  
        self.write(api.public.session_info(sessionId))
