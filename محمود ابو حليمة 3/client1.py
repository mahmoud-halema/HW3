from socket import *

ADD= ('0.0.0.0',9000)
FORMATE="utf-8"

s= socket(AF_INET,SOCK_DGRAM)
# message= input("to Server -> ")

while True:
    message= input("Client -> ")
    s.sendto(message.encode(FORMATE),ADD)
    data,add= s.recvfrom(1024)
    m=data.decode(FORMATE)
    print(f"Server: {m}")




   