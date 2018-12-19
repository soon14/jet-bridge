import tornado.web


class NotFoundHandler(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):
        self.set_status(404)
        self.finish('<h1>Not Found</h1><p>The requested URL {} was not found on this server.</p>'.format(self.request.uri))
