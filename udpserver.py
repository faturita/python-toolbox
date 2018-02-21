import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.2',10000)
print >> sys.stderr, 'Starting up server on %s port %s', server_address
sock.bind(server_address)

while (True):

  data, address = sock.recvfrom(1)
  if (len(data)>0):
     print 'ok'
     sent = sock.sendto('o', address)

  print data

