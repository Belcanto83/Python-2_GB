from protocol import make_response


def send_private_message(request):
    data = dict()

    data['to'] = request.get('to')
    data['from'] = request.get('from')
    data['message'] = request.get('message')

    return make_response(request, 200, data)
