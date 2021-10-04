import socket

HOST = '127.0.0.1'
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        inp = input("Enter Message : ")
        if inp == "exit":
            break
        else:
            inpu = str.encode(inp)
            s.sendall(inpu)
            data = s.recv(1024)
            print('Received', repr(data))
