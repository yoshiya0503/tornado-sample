from tornado import web

class Top(web.RequestHandler):
    def get(self):
        top = 'Hello Top root'
        self.render('top.html', top=top)
