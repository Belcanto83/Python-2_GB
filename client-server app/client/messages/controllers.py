from datetime import datetime

try:
    from .messages import echo_message, private_message, bad_message
except ImportError:
    from messages import echo_message, private_message, bad_message


def make_echo_request():
    message = echo_message

    message['data'] = input('Введите данные echo-запроса: ')

    message['time'] = datetime.now().timestamp()
    return message


def make_private_message():
    message = private_message

    # TODO 2: брать имя своего аккаунта из файла настроек клиента
    message['from'] = 'my_account_name'
    message['to'] = input('Введите имя контакта получателя: ')
    message['message'] = input('Введите текст сообщения: ')

    message['time'] = datetime.now().timestamp()
    return message


def test_bad_request():
    message = bad_message

    message['data'] = input('Введите данные BAD-запроса: ')

    message['time'] = datetime.now().timestamp()
    return message
