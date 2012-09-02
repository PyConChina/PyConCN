#coding: utf-8

import sys, os
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop

port = int(sys.argv[1].split('=')[1])
if port == 0:
    exit(1)

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(0, path)

from uliweb.manage import make_application
application = make_application(project_dir=path)

container = tornado.wsgi.WSGIContainer(application)
http_server = tornado.httpserver.HTTPServer(container, xheaders=True)
http_server.listen(port, '127.0.0.1')
tornado.ioloop.IOLoop.instance().start()
