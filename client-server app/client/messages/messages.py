import json


def presence_message(time, user):
    message_obj = {
        'action': 'presence',
        'time': time,
        'type': 'status',
        'user': {
            'account_name': user['account_name'],
            'status': user['status']
        }
    }
    message_str = json.dumps(message_obj)
    return message_str


def private_message(time, message):
    message_obj = {
        'action': 'msg',
        'time': time,
        'to': 'account_name',
        'from': 'account_name',
        'message': message
    }
    message_str = json.dumps(message_obj)
    return message_str
