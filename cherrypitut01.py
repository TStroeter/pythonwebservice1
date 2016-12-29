import cherrypy


class HelloWorld(object):
    
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    
if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_port': 80,
        'engine.autoreload.on': False,
        'server.shutdown_timeout': 1 })    
    cherrypy.quickstart(HelloWorld())
