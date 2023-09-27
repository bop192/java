import socket



while True:
    HOST = 192.168.1.196 # The server's hostname or IP address
    PORT = 2030 # The port used by the server
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.connect((HOST , PORT))
        while True:
            send_test = input("Input message:")
            if send_test == "exit":
                break
            s.sendall(send_test.encode('utf-8'))
            print(f"Sent: {send_test}")  
            data = s.recv(1025)        
            received_text = data .decode('ulf-8')
            print(f"Received: {received_text}")
