try:
    from messages.actions import action_names
except ImportError:
    from .messages.actions import action_names


def make_request(action_name):
    controller = action_names.get(action_name)
    request = controller()

    return request
