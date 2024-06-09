import socket
import pickle
import random
import rsa

HOST = '127.0.0.1'
PORT = 8080

public_key, private_key = rsa.newkeys(1024)

with socket.socket() as sock:
    sock.connect((HOST, PORT))
    sock.send(pickle.dumps(public_key))

    msg = sock.recv(1024)
    server_public_key = pickle.loads(msg)

    message = "Секретное сообщение".encode()
    encrypted = rsa.encrypt(message, server_public_key)
    sock.send(encrypted)

    encrypted_response = sock.recv(1024)
    response = rsa.decrypt(encrypted_response, private_key)
    print("Ответ:", response.decode())
