__author__ = 'nandi_000'

import socket
import sys
import time
import _thread

class Exchange:

    def __init__(self, Port ):
        self.Connection_Cache = {}
        self.Message_Queue = {}
        self.Max_Data_Size = 1024
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        # Bind the socket to the port
        server_address = ( 'localhost' , Port )
        print( sys.stderr, 'starting up on %s %s ' % server_address )
        sock.bind( server_address )
        sock.listen(1)
        threads = []

        while True:
            # Wait for a connection
            print( sys.stderr, 'waiting for a connection' )
            connection, client_address = sock.accept()
            self.Message_Queue[ client_address ] = []
            self.Connection_Cache[ client_address ] = 1
            # Have a thread process the below code so that accept is available

            #receive data runs in a spanned thread
            New_Thread = _thread.start_new_thread( self.receive_data, ( connection, client_address ) )
            threads.append( New_Thread )

            New_Thread = _thread.start_new_thread( self.send_data, ( connection, client_address ) )
            threads.append( New_Thread )

            #data = receive_data( connection, client_address )
            #Sent Data runs in a separate thread
            #sent = send_data( connection, client_address, data )


    def send_data( self, connection, client_address ):

        while True:
            time.sleep( 15 )
            if client_address not in self.Connection_Cache:
                break;

            if( len( self.Message_Queue[ client_address ] ) ):
                data = self.Message_Queue[ client_address ].pop(0)
                print( "Hi  ", data )
                if data:
                    print( sys.stderr, 'sending data back to the client ', client_address )
                    print( 'sending ', data )
                    a = connection.sendall(data)
                    print( "hi  ", a )
        print( "Exiting Sender Thread " )

    def receive_data( self, connection, client_address ):

        try:
            print( sys.stderr, 'connection from', client_address )
            while True:
                data = connection.recv( self.Max_Data_Size )
                if data:
                #print( "Why am I runnigggg")
                    print( sys.stderr, 'received "', data, '"' )
                    self.Message_Queue[ client_address ].append( data )
                else:
                    del( self.Connection_Cache[ client_address ] )
                    break
        finally:
            print( sys.stderr, 'received all the data' )
            print( "Exiting Receiver Thread " )

Exchange( 10001 )