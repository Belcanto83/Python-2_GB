import json
import yaml
import socket
from argparse import ArgumentParser
import logging
import logging.handlers as handlers
from _thread import start_new_thread
import sqlite3

from actions import resolve
from protocol import validate_request, make_response
from settings import PATH_TO_DB


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


def threaded(c, addr):
    b_request = c.recv(buffer_size)
    request = {}
    try:
        request = json.loads(b_request.decode(encoding))
    except Exception:
        logger.error('Not correct request: %s', b_request)
        exit()
    db_conn = sqlite3.connect(PATH_TO_DB)
    db_conn.text_factory = str
    cursor = db_conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS available_connections 
    ("account_name" text UNIQUE, "ip_host" text, "port_host" text)''')

    cursor.execute(
        'INSERT OR REPLACE INTO available_connections VALUES (?, ?, ?);',
        [request.get('from'), ] + list(addr)
    )
    db_conn.commit()
    db_conn.close()
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

logger = logging.getLogger('server.main')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler = logging.FileHandler('main.log', encoding='utf-8')
file_handler = handlers.TimedRotatingFileHandler('main.log', when='H', interval=24, backupCount=1, encoding='utf-8')

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
    logger.info('Client was detected at %s', address)

    start_new_thread(threaded, (client, address, ))

sock.close()
