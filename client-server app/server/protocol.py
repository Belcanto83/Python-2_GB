from datetime import datetime


def validate_request(raw):
    if 'time' in raw and 'action' in raw:
        return True

    return False


def make_response(request, code, data=None):
    return {
        'action': request.get('action'),
        'time': datetime.now().timestamp(),
        'user': request.get('user'),
        'data': data,
        'code': code,
    }
