import json
import yaml
import socket
from argparse import ArgumentParser

from protocol import make_request


parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
)

args = parser.parse_args()

host = 'localhost'
port = 8000
buffer_size = 1024
encoding = 'utf-8'


if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')

user = {
    'account_name': 'user_1',
    'password': 'admin',
    'status': 'Hello, guys!'
}

try:
    while True:
        sock = socket.socket()
        sock.connect((host, port))
        print(f'Client was started at {host}:{port}')

        action = input('Enter action: ')

        request = make_request(action)

        s_request = json.dumps(request)

        sock.send(s_request.encode(encoding))
        response = sock.recv(buffer_size)
        sock.close()
        print(response.decode(encoding))

except KeyboardInterrupt:
    pass
