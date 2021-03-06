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
import aiohttp
import time
from datetime import datetime
from contextlib import contextmanager
from functools import wraps
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado import httpserver, web
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine
from tornado.options import define, options
from tornado.stack_context import StackContext, NullContext

define('port', default=8000, help='port number', type=int)
define('conf', default='local.py', help='config', type=str)
define('test', type=int)

t = 0

@contextmanager
def calc_time():
    global t
    t = 1
    yield


class BaseHandler(web.RequestHandler):

    def initialize(self):
        print('call init')

    def get_current_user(self):
        return self.get_secure_cookie('user_name')

    def set_default_headers(self):
        self.add_header('version', '1.0.0')
        print('set version to header')

    def on_finish(self):
        print('call end')


class TestHandler(BaseHandler):

    @web.authenticated
    def get(self):
        print(self._headers)
        self.write('end request')

class TestAsyncWith(web.RequestHandler):

    @coroutine
    def get(self):
        with (yield from self.async_check()) as body:
            pass
            #print(body)

    @asyncio.coroutine
    def async_check(self):
        e = asyncio.get_event_loop()
        def hoge():
            global t
            time.sleep(1)
            t = t + 100
            return 'hoge'
        result = None
        #with StackContext(calc_time):
        with calc_time():
            result = yield from e.run_in_executor(None, hoge)
        print(t)

        @contextmanager
        def check():
            yield result
        return check()

class TestWith(web.RequestHandler):

    def get(self):
        with self.check() as body:
            print(body)

    @contextmanager
    def check(self):
        time.sleep(1)
        yield 'hoge'


class LoginHandler(web.RequestHandler):

    def get(self):
        self.write('login page')

if __name__ == '__main__':

    AsyncIOMainLoop().install()
    options.parse_command_line()
    options.parse_config_file(options.conf)
    print(options.conf)
    print(options.port)
    print(options.test)

    settings = {
        'login_url': '/login',
        'cookie_secret': 'hoge'
    }

    application = web.Application([
        ('/', TestHandler),
        ('/login', LoginHandler),
        ('/with', TestWith),
        ('/asyncwith', TestAsyncWith)
    ], **settings)

    server = httpserver.HTTPServer(application)
    server.listen(options.port)
    asyncio.get_event_loop().run_forever()
