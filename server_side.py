from socket import *
import time


HOST = 'localhost'
PORT = 28812
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpTimeSrvrSock = socket(AF_INET,SOCK_STREAM)
tcpTimeSrvrSock.bind(ADDR)
tcpTimeSrvrSock.listen(50)

cday = time.mktime(time.strptime("25/12/2017", "%d/%m/%Y"))


while True:
  print 'waiting for connection...'
  tcpTimeClientSock, addr = tcpTimeSrvrSock.accept()
  print '...connected from:', addr

‹
  while True:
    data = tcpTimeClientSock.recv(BUFSIZE)
    if not data:
      break
    timestamp = time.mktime(time.strptime(data, '%d/%m/%Y'))
    days=round(abs(cday-timestamp))/(24*60*60)
    tcpTimeClientSock.send('%d' % (days))

  tcpTimeClientSock.close()
tcpTimeSrvrSock.close()

