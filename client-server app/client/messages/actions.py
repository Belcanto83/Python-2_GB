try:
    from .controllers import make_echo_request, make_private_message
except ImportError:
    from controllers import make_echo_request, make_private_message


action_names = {
    'echo': make_echo_request,
    'msg': make_private_message,
}
