import socket
import sys
s = socket.socket()
print("Socket successfully created")
port = 3519
s.bind(('', port))
print("socket binded to port")
s.listen(5)
print("socket is listening")
c, addr = s.accept()
print('Got connection from', addr)
data = c.recv(1024)
print("Client: " + data.decode())
if data.decode() == '1':
    print("----------------Chatting-----------------")
    while True:
        while True:
            data = input("Type message to be sent: ")
            c.send(str.encode(data))
            print("Sending: " + data)
            if data == "over":
                break
            if data == "bye":
                break
        if data == "bye":
            break
            s.close()
        while True:
            data = c.recv(1024)
            print("Client: " + data.decode())
            if data.decode() == "over" or data.decode() == "bye":
                break
    exit()
if data.decode() == '2':
    print("--------------File Transferring-------------")
    f = open("a.txt", "wb")
    while True:
        data = c.recv(4096)
        if not data:
            break
        f.write(data)
    f.close()
    print("[+] Download complete!")
    c.close()
    print("[-] Client disconnected")
    a = input("")
sys.exit()