import socket
import sys


def tcp_conn():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

        print("Socket connected sucessful")

        target_host = input("Digite o host desejado:")
        target_port = input("Digite a porta desejada:")

        s.connect((target_host, int(target_port)))
        print()
    except socket.error as e:
        print("Connection Failed!!")
        print(f"ERROR: {e}")


if __name__ == '__main__':
    tcp_conn()
