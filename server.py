import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.bind(('',65432))
    mySocket.listen()

    print('listener running')

    conn, addr = mySocket.accept()

    print('incoming request found')
    with conn:
        print('connected by:', addr)
        while True:
            incomingData = conn.recv(1024)
            if not incomingData:
                break
            conn.sendall(incomingData)