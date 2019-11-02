from protocol import make_response


def send_private_message(request):
    data = dict()

    data['to'] = request.get('to')
    data['from'] = request.get('from')
    data['message'] = request.get('message')

    return make_response(request, 200, data)


def handle_presence_message(request):
    data = 'Connection accepted'

    return make_response(request, 200, data)
