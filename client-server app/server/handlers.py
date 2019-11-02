import json
import logging

from actions import resolve
from middleware import compression_middleware
from protocol import validate_request, make_response


def handle_default_request(raw_request):
    logger = logging.getLogger('server.main')

    request = json.loads(
        raw_request.decode()
    )

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

    return response


@compression_middleware
def encode_response(response):
    return json.dumps(response).encode()
