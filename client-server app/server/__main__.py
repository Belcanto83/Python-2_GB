import json
import yaml
import socket
from argparse import ArgumentParser
import logging
import logging.handlers as handlers
import select
# from _thread import start_new_thread
# import sqlite3

from handlers import handle_default_request

# from settings import PATH_TO_DB


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


# def threaded(c, addr):
#     while True:
#         b_request = c.recv(buffer_size)
#
#         # Попытка регистрации клиентских сообщений и доступных клиентских сокетов в БД
#
#         # request = {}
#         # try:
#         #     request = json.loads(b_request.decode(encoding))
#         # except Exception:
#         #     logger.error('Not correct request: %s', b_request)
#         #     exit()
#         # db_conn = sqlite3.connect(PATH_TO_DB)
#         # db_conn.text_factory = str
#         # cursor = db_conn.cursor()
#         # cursor.execute('''CREATE TABLE IF NOT EXISTS available_connections
#         # ("account_name" text UNIQUE, "ip_host" text, "port_host" text)''')
#         #
#         # cursor.execute(
#         #     'INSERT OR REPLACE INTO available_connections VALUES (?, ?, ?);',
#         #     [request.get('from'), ] + list(addr)
#         # )
#         # db_conn.commit()
#         # db_conn.close()
#
#         b_response = handle_default_request(b_request)
#         c.send(b_response)
#         # c.close()


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

######################################################
connections = []  # Список доступных подключений клиентов
connections_map = {}

######################################################


# Данная функция НЕ портируется отдельно, т.к. использует глобальные переменные! Это плохо..
def add_new_connection():
    # Формируем словарь "connections_map" вида {account_name: socket}
    try:
        client, address = sock.accept()
        logger.info('Client was detected at %s', address)

        # получаем "presence message" от нового клиента
        presence_b_request = client.recv(buffer_size)
        presence_request = handle_default_request(presence_b_request)
        connections_map[presence_request.get('user')] = client
        connections.append(client)
    except OSError:
        pass


def read_requests(r_clients, all_clients):
    # Формируем словарь "requests_map" вида {socket: b_request}
    requests_map = {}
    for r_client in r_clients:
        try:
            b_request = r_client.recv(buffer_size)
            requests_map[r_client] = b_request
            # requests.append(b_request)
        except OSError:
            logger.info('Client %s was disconnected', r_client.getpeername())
            r_client.close()
            all_clients.remove(r_client)

    return requests_map


def write_responses(requests, connections_map, w_clients, all_clients):
    for user in requests.keys():
        user_socket = requests.get(user)




sock = socket.socket()
sock.bind((host, port))
sock.setblocking(False)
sock.listen(5)

logger.info(f'Server was started at {host}:{port}')
# print(f'Server was started at {host}:{port}')

# mainloop()
while True:
    # 1) Добавляем одно новое соединение в список "connections"
    # Формируем словарь вида {account_name: socket}
    add_new_connection()

    if connections:
        rlist, wlist, xlist = select.select(connections, connections, connections, 0)
        # print('r_list: ', rlist)
        # print('w_list: ', wlist)

        # 2) Читаем все запросы из списка всех клиентов
        requests = read_requests(rlist, connections)

        # 3) .............................................
        if requests:
            b_request = requests.pop()
            b_response = handle_default_request(b_request)

            for w_client in wlist:
                try:
                    w_client.send(b_response)
                except OSError:
                    logger.info('Client %s was disconnected', w_client.getpeername())
                    w_client.close()
                    connections.remove(w_client)

    # start_new_thread(threaded, (client, address, ))

# sock.close()
