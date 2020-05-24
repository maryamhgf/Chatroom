import sys
import socket
import select

SOCKET_LIST = []
port = 9090

def server():
    s = socket.socket()
    print ("Socket successfully created")
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 9090))
    print ("socket binded to %s" %(port) )
    s.listen(100)
    print ("socket is listening") 
    # list of connections
    SOCKET_LIST.append(s)
    while True:
        # ready to read sockets.
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
        for sock in ready_to_read:
            # new client.
            if (sock == s): 
                c, addr = s.accept()
                print ('Got connection from', addr )
                # send a thank you message to the client. 
                c.send('Successfully joined the chatroom:)'.encode()) 
                SOCKET_LIST.append(c)
                print ('Got connection from', addr )
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                # receiving data from the socket.
                data = sock.recv(1024)
                data = data.decode()
                if (data):
                    # we have information about socket connection of each client
                    # so we should use sock to find address of each client using getpeername() func.
                    broadcast(s, sock, "<From "+ str(sock.getpeername())+">: " + data) 
    s.close()
    
# broadcast chat messages to all connected clients
# s is new client.
#sock is message sender.
def broadcast (s, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        #s is new connection 
        if socket is not s and socket is not sock :
            try :
                socket.send(message.encode())
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
# running server:
while True:
    server()
sys.exit()

         