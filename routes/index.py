import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

class Server(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

def init_server():
    app = Server(urls, globals())
    app.run(port=3000)
