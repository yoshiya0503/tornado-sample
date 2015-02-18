from tornado import web
from models.test import Test as TestModel


class Test(web.RequestHandler):
    @web.asynchronous
    def get(self):
        test = 'Hello Test root'
        print TestModel().test()
        self.render('test.html', test=test)
