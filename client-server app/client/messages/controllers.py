import hashlib
from datetime import datetime


try:
    from .messages import echo_message, private_message, bad_message, presence_message
except ImportError:
    from messages import echo_message, private_message, bad_message, presence_message


def make_echo_message(account_name):
    message = echo_message

    message['message'] = input('Введите данные echo-запроса: ')

    # message['time'] = datetime.now().timestamp()
    # message['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # hash_obj = hashlib.sha256()
    # hash_obj.update(
    #     str(datetime.now().timestamp()).encode()
    # )
    # message['user'] = hash_obj.hexdigest()

    return message


def make_presence_message(account_name):
    message = presence_message

    return message


def make_private_message(account_name):
    message = private_message

    message['from'] = account_name
    message['to'] = input('Введите имя контакта получателя: ')
    message['message'] = input('Введите текст сообщения: ')

    return message


# Функцию необходимо переработать. "Плохого" сообщения не бывает. Бывает "плохой" request
def test_bad_request(account_name):
    message = bad_message

    message['user'] = account_name
    message['from'] = account_name
    message['message'] = input('Введите данные BAD-запроса: ')

    message['time'] = datetime.now().timestamp()

    return message
