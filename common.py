#!/usr/bin/python3

import socket
import sys
import argparse

HOST = "localhost"
PORT = 9090

data = "sub #hello"

def main():
 
  # Parse defined command line argument
  # Create the parser
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--id", type=str, required = True)
  parser.add_argument("-r", "--sub_port", type = int, required = True)
  parser.add_argument("-h", "--broker_ip",type=str, required = True)
  parser.add_argument("-p", "--port", type = int, required = True)
  parser.add_argument("-f", "--command_file")
  args = parser.parse_args()
  
  try:
  	Thread(target = listening_thread, args = (args,)).start()
  	Thread(target = sending_thread, args = (args,)).start()
  except 




def main():
    # connect to server and send and receive the data twice
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    sock.sendall(bytes(data +  "\n", "utf-8"))

    # receive the data
    while True:
        try:
            received = str(sock.recv(1024), "utf-8")
            print("Received: " + received)
        except:
            print("Error/Disconnect")

if __name__ == "__main__":
    main()
    
    
    
