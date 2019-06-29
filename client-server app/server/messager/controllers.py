from protocol import make_response


def send_private_message(request):
    address = input('Введите адресата личного сообщения: ')
    message = input('Введите текст личного сообщения: ')

