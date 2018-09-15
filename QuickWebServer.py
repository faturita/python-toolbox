# coding: latin-1
#
# Very simple Web Server.
#
#
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"
server_address = ('0.0.0.0', 8000)
httpd = ServerClass(server_address, HandlerClass)

print('Waiting on port 8000...')

httpd.serve_forever()
