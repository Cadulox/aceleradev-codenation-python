import jwt


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        decode = jwt.decode(token, 'acelera', algorithms='HS256')
    except jwt.InvalidTokenError:
        decode = {'error': 2}
    return decode
