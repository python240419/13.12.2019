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
socket_.connect((TCP_IP, TCP_PORT))

MESSAGE = { 'command': 'Hello'}
n = json.dumps(MESSAGE)
bytes = str.encode(n)
socket_.send(bytes)
data = str(socket_.recv(BUFFER_SIZE), 'utf-8')
print(data)



