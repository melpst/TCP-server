import socket
import sys

#Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind server address to port
server_address = ('10.1.1.173', 8000)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    #Wait for connection
    print >> sys.stderr, 'waiting for connection'
    connection, client_address = sock.accept()

    try:
	print sys.stderr, 'connection from', client_address

        #Receive the data in small chunk and retranmit it
        while True:
            connection.setblocking(0)
            data = connection.recv(16)
            if data:
                print >> sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        #Clean up the connection
        connection.close()
