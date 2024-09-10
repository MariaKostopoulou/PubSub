#!/usr/bin/python3

import socket
import sys
import argparse
from threading import Thread


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
  	Thread(target = receive_thread, args = (args,)).start()
  	Thread(target = send_topic_thread, args = (args,)).start()
  except:
  	sys.exit(0)



def send_topic_thread(args):
"""Thread used for sending topics to broker."""

    # Connect to broker
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.broker_ip, args_port))
    
    sock.sendall(bytes(data +  "\n", "utf-8"))



def receive_topic_thread(args):
   sock.accept()

    # receive the data
    while True:
        try:
            received = str(sock.recv(1024), "utf-8")
            print("Received: " + received)
        except:
            print("Error/Disconnect")



if __name__ == "__main__":
    main()
    
    
    
