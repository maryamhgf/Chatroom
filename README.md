# Chatroom
Implementation of a chatroom using socket programming. There is one server which can be connected by an arbitrary number of clients.

Here is how to run the server and the client on linux machines:

Server:

Open the terminal and cd to the directory of the codes.

Run the server by: “python chat_server.py -sp 9090”.

(The server will be run on port 9090)

Client:

Open another terminal and cd to the directory of the codes.

Run the client by: “python client.py -sip 127.0.0.1 -sp 9090 .

(Connecting to a server running on localhost and port number 9090)

For every new client, open a new terminal and type the previous command.

When a client types a message in the terminal, all the clients in that chatroom will see this message: < From Client_ip , Client_port>: Message!.
