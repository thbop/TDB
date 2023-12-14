import json
from base64 import urlsafe_b64encode as b64e

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from cryptography.fernet import InvalidToken

# https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
# https://bard.google.com

def _derive_key(key: str) -> bytes:
    """Derive a secret key from a given password"""
    print(key)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=b'Saucy salt that is consistent',
        iterations=100_000, backend=default_backend())
    return b64e(kdf.derive(key.encode()))

def encrypt(key, data):
    fernet = Fernet(_derive_key(key))
    data = fernet.encrypt(json.dumps(data).encode())
    return json.dumps(data.decode())

def decrypt(key, data):
    fernet = Fernet(_derive_key(key))
    data = json.loads(data).encode()
    try:
        return json.loads(fernet.decrypt(data).decode())
    except InvalidToken:
        return None

if __name__ == '__main__':

    data = {'jo':'bar'}
    password = 'mypass'
    key = _derive_key(password)
    enc = encrypt(key, data)

    print(enc, decrypt(key, enc))

    # password = 'mypass'

    # # key = Fernet.generate_key()
    # fernet = Fernet(_derive_key(password.encode()))
    # fernet2 = Fernet(_derive_key('mypass'.encode()))


    # message = "This is a secret message!"
    # encrypted_message = fernet.encrypt(message.encode())

    # try:
    #     decrypted_message = fernet2.decrypt(encrypted_message).decode()
    # except InvalidToken:
    #     decrypted_message = None

    # print(f"Original message: {message}")
    # print(f"Encrypted message: {encrypted_message}")
    # print(f"Decrypted message: {decrypted_message}")

