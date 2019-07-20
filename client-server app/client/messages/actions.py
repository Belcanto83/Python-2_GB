try:
    from .controllers import make_echo_request, make_private_message, test_bad_request
except ImportError:
    from controllers import make_echo_request, make_private_message, test_bad_request


action_names = {
    'echo': make_echo_request,
    'msg': make_private_message,
    'bad_request': test_bad_request
}
