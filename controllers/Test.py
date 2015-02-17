from tornado import web

class Test(web.RequestHandler):
    @web.asynchronous
    def get(self):
        test = 'Hello Test root'
        self.render('test.html', test=test)
