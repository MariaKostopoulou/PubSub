#!/usr/bin/python3

import threading
import socket
import sys


HOST = "localhost"
P_PORT = 9000
S_PORT = 9090


# thread for publisher
def pubthread():
    # set up for publisher
    pub_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pub_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    pub_sock.bind((HOST, P_PORT))
    pub_sock.listen(10)
    print("Broker listening Pubs on %s %d" %(HOST, P_PORT))

    conn, addr = pub_sock.accept()
    print("Pub Connected : " + addr[0] + ":" + str(addr[1]))

    while True:
        try:
            data = conn.recv(1024).strip()
            print("Received from Pub: " + str(data))
            conn.sendall(bytes("OK", "utf-8"))
        except:
            print("Pub Disconnected")
            break

# thread for subscriber
def subthread():
    # set up for subscriber
    sub_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sub_sock.bind((HOST, S_PORT))
    sub_sock.listen(10)
    print("Broker listening Subs on %s %d" %(HOST, S_PORT))

    conn, addr = sub_sock.accept()
    print("Sub Connected : " + addr[0] + ":" + str(addr[1]))

    while True:
        try:
            data = conn.recv(1024).strip()
            print("Received from Sub: " + str(data))
            conn.sendall(bytes("OK", "utf-8"))

            # send the sub some data
            conn.sendall(bytes("\nsome data for you", "utf-8"))
        except:
            print("Sub Disconnected")
            break



def main():
    try:
        threading.Thread(target=pubthread).start()
        threading.Thread(target=subthread).start()

    except KeyboardInterrupt as msg:
        sys.exit(0)


if __name__ == "__main__":
    main()
