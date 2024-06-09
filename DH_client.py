import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

p = 7
g = 5

a = random.randint(1, p-1)
A = pow(g, a, p)

with socket.socket() as sock:
    sock.connect((HOST, PORT))
    sock.send(pickle.dumps((p, g, A)))

    msg = sock.recv(1024)
    p, g, B = pickle.loads(msg)

    K = pow(B, a, p)
    print("Общий секрет:", K)
