#coding=utf-8
import socket
from multiprocessing.dummy import Pool as ThreadPool
import time

#server_IP = '127.0.0.1'
server_IP = '106.14.161.204'
server_Port = 3389

def tryOnceConnect(args):
    print("thread args = %s"%args)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_IP, server_Port))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send((b'exit'))
    s.close()

#main
args = []
for i in range(0,1024):
    args.append(i)

pool = ThreadPool(1024)
time_start = time.time()
result = pool.map(tryOnceConnect, args)
pool.close()
pool.join()
time_end = time.time()
print "%s 100线程 共消耗："%str(time_end-time_start)