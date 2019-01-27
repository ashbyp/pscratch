import socket


def server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        while True:
            s.listen()
            conn, address = s.accept()
            with conn:
                print('Connected by', address)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print('No data, exit')
                        break
                    conn.sendall(data)


def client(host, port, msg='Hello, World!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(bytes(msg, 'utf8'))
        data = s.recv(1024)
        print('Received', repr(data))


