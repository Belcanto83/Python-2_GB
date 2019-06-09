# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     pass

import yaml
import socket
from argparse import ArgumentParser

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

try:
    sock = socket.socket()
    sock.connect((host, port))
    print(f'Client was started on {host}:{port}')
    data = input('Enter data: ')
    sock.send(data.encode(encoding))
    response = sock.recv(buffer_size)
    print(response.decode(encoding))
except KeyboardInterrupt:
    pass
