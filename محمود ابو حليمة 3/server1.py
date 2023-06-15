from socket import *  

ADD= ('0.0.0.0',9000)
FORMATE="UTF-8"

s= socket(AF_INET,SOCK_DGRAM)
s.bind(ADD)

print("Server is Listening ...")
while True:
    data,add= s.recvfrom(1024)
    m=data.decode(FORMATE)
    print(f"Client: {m}")
    d=input("Server: ")
    s.sendto(d.encode(FORMATE),add)

