#!/usr/bin/python
# coding: utf-8

import logging

import tornado.ioloop
import tornado.web
import tornado.httpserver

import handlers
import settings

urls = [
        (r'/blogtypes', handlers.BlogTypes)
       ]

app = tornado.web.Application(urls)
    
def run_server():
    logging.info('Starting HabrAPI on http://{address}:{port}/'.format(**settings.REST_SERVER))
    
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(**settings.REST_SERVER)    
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        logging.info('Stopping server: Interrupted')
        exit()

if __name__ == '__main__':
    run_server()
