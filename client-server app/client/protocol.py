try:
    from messages.actions import action_names
except ImportError:
    from .messages.actions import action_names

from datetime import datetime

from __main__ import encoding
from middleware import compression_middleware


@compression_middleware(encoding)
def make_request(action_name, account_name=None):
    controller = action_names.get(action_name)
    # Возможно, что в controller не нужно передавать аргумент account_name
    data = controller(account_name)

    return {
        'action': action_name,
        'time': datetime.now().timestamp(),
        'user': account_name,
        'data': data,
    }
