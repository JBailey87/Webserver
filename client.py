import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect(('jbpage',65432))
    
    mySocket.sendall(b'Hello world')