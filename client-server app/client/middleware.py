import zlib
import json


def compression_middleware(encoding):
    def wrap(func):
        def decorator(action, *args, **kwargs):
            request = func(action, *args, **kwargs)
            s_request = json.dumps(request)
            b_request = zlib.compress(s_request.encode(encoding))
            return b_request
        return decorator
    return wrap
