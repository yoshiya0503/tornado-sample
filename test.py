#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Asyncio And Tornado Sample

we build web app using both tornado and asyncio.
Instead of IOLoop in tornado, we try to use event-loop of asyncio.
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '10 Jun 2015'

import asyncio
from tornado.platform.asyncio import AsyncIOMainLoop
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define('port', default=8000, help='this is help', type=int)

class Index(tornado.web.RequestHandler):
    '''
    RequestHandler test
    '''

    @tornado.gen.coroutine
    def get(self):
        '''
        get: GET method
            We have to use tornado.gen.coroutine to keep high performance.
        '''

        # using asyncHTTP of tornado
        #http = tornado.httpclient.AsyncHTTPClient()
        #yield http.fetch('http://google.com')
        #yield http.fetch('http://google.com')
        #yield http.fetch('http://google.com')

        # using coroutine of asyncio
        tasks = [
            asyncio.async(self.a()),
            asyncio.async(self.b()),
            asyncio.async(self.c()),
        ]
        result = yield from asyncio.gather(*tasks)
        print(result)
        self.write('end request')

    @asyncio.coroutine
    def a(self):
        '''
        a: sample method
            This method will run asyncronouncely by using asyncio.coroutine
            and run_in_executor.
            The run_in_executor will convert blocking method to no-blocking one.
        '''
        context = asyncio.get_event_loop()
        http_client = tornado.httpclient.HTTPClient()
        yield from context.run_in_executor(None, http_client.fetch, "http://www.google.com/")
        return 'a'

    @asyncio.coroutine
    def b(self):
        context = asyncio.get_event_loop()
        http_client = tornado.httpclient.HTTPClient()
        yield from context.run_in_executor(None, http_client.fetch, "http://www.google.com/")
        return 'b'

    @asyncio.coroutine
    def c(self):
        context = asyncio.get_event_loop()
        http_client = tornado.httpclient.HTTPClient()
        yield from context.run_in_executor(None, http_client.fetch, "http://www.google.com/")
        return 'c'


if __name__ == '__main__':

    #We use event loop of asyncio instead of tornado IOLoop
    AsyncIOMainLoop().install()
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        ('/', Index)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    #tornado.ioloop.IOLoop().instance().start()
    asyncio.get_event_loop().run_forever()
