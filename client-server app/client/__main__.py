import json
import yaml
import socket
from argparse import ArgumentParser
from datetime import datetime
try:
    from .messages import presence_message
except ImportError:
    from messages import presence_message


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

# print(presence_message('12/06/2019', {'account_name': 'ggH', 'status': 'good'}))

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
    sock = socket.socket()
    sock.connect((host, port))
    print(f'Client was started at {host}:{port}')
    action = input('Enter action: ')
    data = input('Enter data: ')
    request = {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data
    }
    s_request = json.dumps(request)

    sock.send(s_request.encode(encoding))
    response = sock.recv(buffer_size)
    print(response.decode(encoding))
except KeyboardInterrupt:
    pass
