import socket
import sys
import time
from Crypto.PublicKey import RSA

#Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind server address to port
server_address = ('127.0.0.1', 8000)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    #Wait for connection
    print >> sys.stderr, 'waiting for connection'
    connection, client_address = sock.accept()

    try:
        print sys.stderr, 'connection from', client_address

        key = open('../.ssh/id_rsa.pub', 'rb').read()
        publicKey = RSA.importKey(key)

        message = 'asdfghjkl;\'qwertyuiop[]zxcvbnm,./1234567890-='
        cipher = publicKey.encrypt(message, 32)[0]
        print cipher
        connection.sendall(cipher)

        decrypted_message = connection.recv(2048)
        print "decrypted message is %s" % decrypted_message

    finally:
        #Clean up the connection
        connection.close()