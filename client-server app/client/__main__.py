import json
import yaml
import zlib
import socket
from argparse import ArgumentParser

import logging
import client_log_config
from protocol import make_request


parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
)
parser.add_argument(
    '-m', '--mode', type=str, default='w',
    help='Sets client mode'
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

logger = logging.getLogger('client.main')

user = {
    'account_name': 'user_1',
    'password': 'admin',
    'status': 'Hello, guys!'
}

try:
    sock = socket.socket()
    sock.connect((host, port))
    logger.info('Client was started at %s:%s', host, port)

    if args.mode == 'w':
        while True:
            action = input('Enter action: ')

            request = make_request(action)
            s_request = json.dumps(request)
            b_request = zlib.compress(s_request.encode(encoding))
            sock.send(b_request)
    else:
        while True:
            response = sock.recv(buffer_size)
            b_response = zlib.decompress(response)
            print(b_response.decode(encoding))

except KeyboardInterrupt:
    pass
