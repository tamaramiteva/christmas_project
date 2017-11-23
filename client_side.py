from socket import *

HOST = 'localhost'
PORT = 28812
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpTimeClientSock = socket(AF_INET, SOCK_STREAM)
tcpTimeClientSock.connect(ADDR)

data = raw_input('Put the date you like to send to server in order DD/MM/YYYY: \n')

tcpTimeClientSock.send(data)

data_received = tcpTimeClientSock.recv(BUFSIZE)
  
print data_received + " days until christmas."

tcpTimeClientSock.close()
