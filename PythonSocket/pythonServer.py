import socket
import time
import threading
#server_IP = '127.0.0.1'
server_IP = '106.14.161.204'
server_Port = 3389

def tcplink(sock, addr):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == 'exit':
            break
        sock.send(('Hello, %s!'% data.decode("utf-8")).encode('utf-8'))
    #socket.close()
    print("Connection from %s:%s closed" % addr)

#main
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server_IP, server_Port))

s.listen(100)
print("Waiting for connection...")

while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

