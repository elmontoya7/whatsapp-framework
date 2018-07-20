import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

def init_server():
    app = web.application(urls, globals())
    app.run()
