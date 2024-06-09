import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()

    msg = conn.recv(1024)
    p, g, A = pickle.loads(msg)

    b = random.randint(1, p-1)
    B = pow(g, b, p)

    K = pow(A, b, p)
    print("Общий секрет:", K)

    conn.send(pickle.dumps((p, g, B)))
