from tornado import web, ioloop
import os
import controllers

if __name__ == '__main__':
    app = web.Application(
        controllers.getRouting(),
        template_path=os.path.join(os.path.dirname(__file__), 'views')
    )

    app.listen(8888)
    ioloop.IOLoop.instance().start()
