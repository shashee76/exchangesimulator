__author__ = 'nandi_000'

import socket
import sys

def send_data( connection, client_address, data ):
    print( 'sending ', data )
    if data:
        print( sys.stderr, 'sending data back to the client ', client_address )
        print( 'sending ', data )
        connection.sendall(data)
        return( True )

    return( False )

def receive_data( connection, client_address ):

    alldata = ""

    try:
        print( sys.stderr, 'connection from', client_address )
        data_array = []
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            if data:
                data_array.append( data )
                connection.sendall(data)
                print( sys.stderr, 'received "', data, '"' )
            else:
                print( sys.stderr, "received all the data")
                break

        print( data_array )
        alldata = ''.join( data_array )


    finally:
        return( alldata )

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10002)
print( sys.stderr, 'starting up on %s %s ' % server_address )
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    print( sys.stderr, 'waiting for a connection' )
    connection, client_address = sock.accept()

    # Have a thread process the below code so that accept is available

    data = receive_data( connection, client_address )
    #sent = send_data( connection, client_address, data )

    connection.close()
