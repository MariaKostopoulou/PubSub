#!/usr/bin/python3

import socket
import sys

HOST = "localhost"
PORT = 9000

data = "pub #hello there "


def main():
    # connect to server and send and receive the data twice
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    i = 0

    while True:
        sock.sendall(bytes(data + str(i) +  "\n", "utf-8"))

        # receive the data
        received = str(sock.recv(1024), "utf-8")
        print("Received: " + received)

        i += 1 
        if i == 2 : break


if __name__ == "__main__":
    main()
