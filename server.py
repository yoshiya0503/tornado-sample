import tornado.ioloop
import tornado.web
import cont

class Main(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello Tornado')

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Main)
    ])

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
