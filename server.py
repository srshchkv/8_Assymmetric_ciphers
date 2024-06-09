import socket
import pickle
import rsa

HOST = '127.0.0.1'
PORT = 8080

public_key, private_key = rsa.newkeys(1024)

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    msg = conn.recv(1024)
    client_public_key = pickle.loads(msg)

    conn.send(pickle.dumps(public_key))

    encrypted_message = conn.recv(1024)
    message = rsa.decrypt(encrypted_message, private_key)
    print("Получено сообщение:", message.decode())

    response = "Привет, клиент!".encode()
    encrypted_response = rsa.encrypt(response, client_public_key)
    conn.send(encrypted_response)
