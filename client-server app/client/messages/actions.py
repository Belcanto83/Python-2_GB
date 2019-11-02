try:
    from .controllers import make_echo_message, make_private_message, make_presence_message, test_bad_request
except ImportError:
    from controllers import make_echo_message, make_private_message, make_presence_message, test_bad_request


action_names = {
    'echo': make_echo_message,
    'presence': make_presence_message,
    'msg': make_private_message,
    'bad_request': test_bad_request,
}
