import sys
import socket
import select
 
def client():
    s = socket.socket()
    s.connect(('127.0.0.1', 9090))
    # receive welcome message from the server 
    print (s.recv(1024).decode())
    print ("Welcome to chatroom!")
    while True:
        socket_list = [sys.stdin, s]
        # ready to read sockets:
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        for sock in read_sockets:            
            if sock == s:
                # incoming message from server
                data = sock.recv(1024)
                data = data.decode()
                if not data :
                    print ("Something get wrong. Try again!")
                    sys.exit()
                else :
                    sys.stdout.write(data)                
            else :
                #messaging:
                message = sys.stdin.readline()
                s.send(message.encode()) 

#running client:
while True:
    client()
sys.exit()
