from datetime import datetime
import logging
from actions import get_server_actions

# logger = logging.getLogger('server.main')


def validate_request(raw):
    if 'time' in raw and 'action' in raw:
        requested_action = raw.get('action')
        server_actions = [action.get('action') for action in get_server_actions()]
        if requested_action in server_actions:
            return True
        # else:
        #     logger.error('Not correct action name: %s', requested_action)

    return False


def make_response(request, code, data=None):
    return {
        'action': request.get('action'),
        'time': datetime.now().timestamp(),
        'user': request.get('user'),
        'data': data,
        'code': code,
    }
