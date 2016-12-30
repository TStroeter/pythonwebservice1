import cherrypy
import JinjaDemo

class CherryPyServer(object):
    
    @cherrypy.expose
    def index(self):
        return JinjaDemo.jinjaDemo()
    
if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_port': 8090,
        'engine.autoreload.on': False,
        'server.shutdown_timeout': 1 })    
    cherrypy.quickstart(CherryPyServer())
