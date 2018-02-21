# coding: latin-1

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"
server_address = ('0.0.0.0', 8000)
httpd = ServerClass(server_address, HandlerClass)

httpd.serve_forever()
