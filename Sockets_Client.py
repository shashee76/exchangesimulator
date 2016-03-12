__author__ = 'nandi_000'

import socket
import sys
import time
import _thread

class Client:

    def __init__(self):
        self.Sender_Active = True
        self.Receiver_Active = True
        self.Max_Data_Size = 1024

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10001)
        print( sys.stderr, 'connecting to %s port %s' % server_address )
        sock.connect(server_address)
        threads = []

        New_Thread = _thread.start_new_thread( self.receive_data, ( sock, "" ) )
        threads.append( New_Thread )

        New_Thread = _thread.start_new_thread( self.send_data, ( sock, "" ) )
        threads.append( New_Thread )

        while( self.Active() ):
            time.sleep( 10 )

        sock.close()

    def send_data( self, sock, a ):
        try:
            message = 'This is the message.  It will be repeated.'
            print( sys.stderr, 'sending "%s"' % message )
            message = bytes(message, "utf-8")
            sock.sendall(message)

        finally:
            print( "Sent all the data" )

        self.Sender_Active = False

        print( "Exiting Sender Thread")

    def receive_data( self, sock, a ):
        try:
            print( "receiving data")
            while True:
                data = sock.recv( self.Max_Data_Size )
                if( data ):
                    #print( "Why am I runnigggg")
                    self.Receiver_Active = False #Close the connection given that the data is received
                    print( sys.stderr, 'received "', data, '"' )

                else:
                    break

                if( self.Receiver_Active == False ):
                    break

        finally:
            print( sys.stderr, 'received all the data' )
            print( "Exiting Receiver Thread " )

    def Active(self):
        return( self.Sender_Active or self.Receiver_Active )


Client()

"""

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print( sys.stderr, 'connecting to %s port %s' % server_address )
sock.connect(server_address)



try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    print( sys.stderr, 'sending "%s"' % message )
    message = bytes(message, "utf-8")
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print( sys.stderr, 'received "%s"' % data )

finally:
    print( sys.stderr, 'closing socket' )
    #Handle the shutdown well
    #sock.shutdown()
    sock.close()
    time.sleep( 60 )

"""