from faker import Faker
import socket
import os
import json_helper

def init():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    json_file = json_helper.get()
    server_address = json_file['server_address']

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('Starting up on {}'.format(server_address))

    sock.bind(server_address)
    sock.listen(1)

    return sock

def main(sock):
    while True:
        print('Waiting connection')

        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            json_file = json_helper.get()
            buffer_size = int(json_file['buffer_size'])

            while True:
                data = connection.recv(buffer_size)
                data_str =  data.decode(json_file['character_code'])

                print('Received ' + data_str)

                if data:
                    response = create_faker_val(data_str)
                    connection.sendall(response.encode())

                else:
                    print('no data from', client_address)
                    break
        finally:
            print("Closing current connection")
            connection.close()

# if you add dict pattern, you add a value to dict variable
def create_faker_val(val):
    fake = Faker()

    dict = {
        'name': fake.name(),
        'address': fake.address()
    }

    return dict.get(val, fake.country())

sock = init()
main(sock)