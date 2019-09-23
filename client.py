import socket
import sys
s = socket.socket()
port = int(input("Enter the port number: "))
if port!= 3519:
    print("Port number incorrect, please retry")
    a = input("Press enter to retry")
if port == 3519:
    print("Port number correct\n")
    s.connect(('127.0.0.1', port))
    print("1. Messaging")
    print("2. File Transferring")
    print("3. Exit\n")
    message = input("Choose one option: ")
    s.send(str.encode(message))
    if message == '1':
        print("-------Chatting--------")
        while True:
            while True:
                message = s.recv(1024)
                print("Server: " + message.decode())
                if message.decode() == "over":
                    break
                if message.decode() == "bye":
                    break
            while True:
                message = input("Type message to be sent: ")
                s.send(str.encode(message))
                print("Sending: " + message)
                if message == "over" or message == "bye":
                    break
            if message == "bye":
                break
                c.close()
        exit()
    if message == '2':
        print("-------File Transferring-------")
        print("[+] Connected with Server")
        f_send = "a.txt"
        with open(f_send, "rb") as f:
            print("[+] Sending file...")
            data = f.read(1024)
            s.sendall(data)
            s.close()
            print("[-] Disconnected")
            a = input("")
        sys.exit(0)

    else:
        print("Exiting...")
        a = input("")