import socket
import sys
import json_helper

def init():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    json_file = json_helper.get()
    server_address = json_file['server_address']

    print('connecting to {}'.format(server_address))

    try:
        sock.connect(server_address)
    except socket.error as err:
        print(err)
        sys.exit(1)

    return sock

def main(sock):
    try:
        val = input('please input value: ')

        json_file = json_helper.get()

        sock.sendall(val.encode(json_file['character_code']))     
        sock.settimeout(2)

        try:
            while True:
                buffer_size = int(json_file['buffer_size'])
                data = str(sock.recv(buffer_size))

                if data:
                    print('Server response: ' + data)
                else:
                    break

        except(TimeoutError):
            print('Socket timeout, ending listening for server messages')

    finally:
        print('closing socket')
        sock.close()

sock = init()
main(sock)