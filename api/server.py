#!/usr/bin/python
# coding: utf-8

import logging

import tornado.ioloop
import tornado.web
import tornado.httpserver

from habroid.api.handlers import BlogTypes, BlogList
import habroid.api.settings as settings

urls = [(r'/blogtypes', BlogTypes),
        (r'/bloglist', BlogList),
       ]

app = tornado.web.Application(urls)
    
def run_server():
    logging.info('Starting Habroid API on http://{address}:{port}/'.format(**settings.REST_SERVER))
    
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(**settings.REST_SERVER)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        logging.info('Stopping server: Interrupted')
        exit()

if __name__ == '__main__':
    run_server()
