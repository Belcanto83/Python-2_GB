import json
import yaml
import socket
from argparse import ArgumentParser
from actions import resolve
from protocol import validate_request, make_response


parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
)

args = parser.parse_args()

host = '0.0.0.0'
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
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server was started at {host}:{port}')

    while True:
        client, address = sock.accept()
        print(f'Client was detected at {address}')
        b_request = client.recv(buffer_size)
        request = json.loads(b_request.decode(encoding))
        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    print(err)
                    response = make_response(request, 500, 'Internal server error')
            else:
                response = make_response(request, 404, 'Action not found')
        else:
            response = make_response(request, 400, 'Wrong request')

        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))
        client.close()
except KeyboardInterrupt:
    pass
