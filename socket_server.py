import threading
import sys
import json
import queue
import os
import socket
import time

TCP_IP = '127.0.0.1' # localhost -- myself
TCP_PORT = 6736
BUFFER_SIZE = 1024

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.bind((TCP_IP, TCP_PORT))
socket_.listen(100)

conn, addr = socket_.accept()
print("Connection address:", addr)
data = conn.recv(BUFFER_SIZE)
print(data)
data_as_json = json.loads(str(data, 'utf-8'))
print(data_as_json)
print(data_as_json['command'])
bytes = str.encode("Server got your request...")
conn.send(bytes)
