import socket
import sys

HOST = ''
PORT = 8888


def main():
    s = socket.socket()
    try:
        s.bind((HOST, PORT))
    except:
        print("Error")
        sys.exit()

    s.listen(10)

    while True:
        conn, addr = s.accept()
        logic(conn)


def logic(conn):
    conn.sendall(b"Hello, what is your age? Enter here: ")
    age = int(conn.recv(50).strip())
    print("Person is age %d" % age)
    conn.sendall(b"Thank you. You are old.")
    conn.close()


if __name__ == "__main__":
    main()
