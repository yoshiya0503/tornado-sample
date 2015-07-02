#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Middlewares
this is test for auth and custom-header
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '02 Jul 2015'

import asyncio
from functools import wraps
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado import httpserver, web
from tornado.options import define, options

define('port', default=8000, help='port number', type=int)


class BaseHandler(web.RequestHandler):

    def initialize(self):
        print('call init')

    def set_default_headers(self):
        self.add_header('version', '1.0.0')
        print('set version to header')

    def on_finish(self):
        print('call end')


class TestHandler(BaseHandler):

    def get(self):
        print(self._headers)
        self.write('end request')


if __name__ == '__main__':

    AsyncIOMainLoop().install()
    options.parse_command_line()

    application = web.Application([
        ('/', TestHandler)
    ])

    server = httpserver.HTTPServer(application)
    server.listen(options.port)
    asyncio.get_event_loop().run_forever()
