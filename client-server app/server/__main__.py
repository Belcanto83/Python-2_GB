import json
import yaml
import socket
from argparse import ArgumentParser
import logging
from _thread import start_new_thread

from actions import resolve
from protocol import validate_request, make_response


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


def threaded(c):
    b_request = c.recv(buffer_size)
    request = json.loads(b_request.decode(encoding))
    if validate_request(request):
        action_name = request.get('action')
        controller = resolve(action_name)
        if controller:
            try:
                response = controller(request)
            except Exception as err:
                logger.critical(err)
                # print(err)
                response = make_response(request, 500, 'Internal server error')
        else:
            logger.error(f'404 - request not found: {request}')
            response = make_response(request, 404, 'Action not found')
    else:
        logger.error(f'400 - wrong request: {request}')
        response = make_response(request, 400, 'Wrong request')
    s_response = json.dumps(response)
    c.send(s_response.encode(encoding))
    c.close()


if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')

logger = logging.getLogger('main')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('main.log', encoding='utf-8')

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.DEBUG)

sock = socket.socket()
sock.bind((host, port))
sock.listen(5)

logger.info(f'Server was started at {host}:{port}')
# print(f'Server was started at {host}:{port}')

while True:
    client, address = sock.accept()
    print(f'Client was detected at {address}')
    start_new_thread(threaded, (client, ))

sock.close()
