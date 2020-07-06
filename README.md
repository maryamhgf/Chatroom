# Chatroom
Implementation of a chatroom using socket programming. There are one server and arbitrary number of clients can join.

Server:(Ubuntu)

1. Open terminal and type cd "directory of the codes".

2. The server will be run in port 9090(you can change it in the code.)

3. Type python chat_server.py -sp 9090 in the terminal.

Client:(Ubuntu)

1. Open a new terminal and type cd "directory of the codes".

2. Type python client.py sip- server-ip sp- 9090 (For example: python client.py sip- 9090 sp- 9090)

For every new client open a new terminal and type the previous command.

When a client type a message in the terminal, for all the clients in that chatroom < From Client_ip , Client_port>: Message! will be shown.
