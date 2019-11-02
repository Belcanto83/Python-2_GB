from .controllers import send_private_message, handle_presence_message

action_names = [
    {'action': 'msg', 'controller': send_private_message},
    {'action': 'presence', 'controller': handle_presence_message},
]
