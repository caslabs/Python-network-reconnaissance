import socket

#finds the IP of the entered domain name
print("convert to domain name's ipadd")
print("example: google.com")

try:
    while True:
        data = raw_input("enter domain name : ")
        print(socket.gethostbyname(data))
except KeyboardInterrupt:
    print("exiting")
    pass
