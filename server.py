import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000
    server.bind((server_ip, port))
    server.listen(0)
    print(f"Listening on {server_ip}: {port}")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"Recieved: {request}")

        response = "accepted".encode("utf-8")
        client_socket.send(response)

    client_socket.close()
    print("Connection to client closed")

    server.close()

run_server()