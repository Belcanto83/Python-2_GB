echo_message = {
    'action': 'echo',
    'time': None,

    'data': None,
}


presence_message = {
    'action': 'presence',
    'time': None,

    'type': 'status',
    'user': {
        'account_name': None,
        'status': None,
    },
}


private_message = {
    'action': 'msg',
    'time': None,

    'to': None,
    'from': None,
    'message': None
}


bad_message = {
    'action': 'bad_request',
    'time': None,

    'data': None,
}
