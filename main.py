import socket
import threading

target = "127.0.0.1"


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Set a timeout for the connection attempt
    result  = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    s.close()


if __name__ == "__main__":

    for port in range(1, 1025):  # Scanning ports from 1 to 1024
        thread = threading.Thread(target=scan_port, args=(port,))

        thread.start()