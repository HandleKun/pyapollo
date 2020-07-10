import base64
import hmac
from hashlib import sha1

def authorization(appid, sign):
    return 'Apollo {}:{}'.format(appid, sign)

def signature(timestamp, path, secret):
    to_sign = timestamp + '\n' + path
    hmac_code = hmac.new(secret.encode(), to_sign.encode(), sha1).digest()
    return base64.b64encode(hmac_code).decode()