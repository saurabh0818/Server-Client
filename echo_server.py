import socket




def Soc_Server():
    HOST = '192.168.0.103'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print("coonectio : ",conn)
        print("Address : ",addr)
        with conn:
            print('Connected by', addr)

            while True:
                inp = "Welcome to eScan Server (Created By Saurabh Upadhyay) !!!"
                inpu = str.encode(inp)
                conn.sendall(inpu)
                data = conn.recv(1024)
                print('Received', repr(data))
                if not data:
                    s.close()
                    print("Thank You !!")
                    break;


                else:
                    with open("response.txt",'a',encoding = 'utf-8') as f:
                        f.write("{}\n".format(data))

                #inp = input("Enter Message : ")
                inp = "Successfull Received"
                inpu = str.encode(inp)
                conn.sendall(inpu)





if __name__ == "__main__":
    Soc_Server()
