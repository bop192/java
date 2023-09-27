import socket
import turtle

HOST = "192.168.1.196"  # Địa chỉ IP của máy chủ (đặt lại thành địa chỉ IP của máy chủ của bạn)
PORT = 2030   # Cổng của máy chủ

def draw_circle(color, radius, name):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.write(name, font=("Arial", 15, "normal"))
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")

        if data.startswith("CREATE"):
            parts = data.split(" ")
            if len(parts) >= 4:
                color = parts[1]
                radius = int(parts[2])
                name = parts[3]
                draw_circle(color, radius, name)
                client_socket.sendall("Circle created successfully".encode('utf-8'))
            else:
                client_socket.sendall("Invalid CREATE command".encode('utf-8'))
        else:
            client_socket.sendall("Invalid command".encode('utf-8'))

        client_socket.close()

if _name_ == "_main_":
    turtle.speed(1)
    main()