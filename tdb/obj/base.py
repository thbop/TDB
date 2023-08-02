from ..utils.encryption import encrypt, decrypt
import json

class Base:
    def __init__(self):
        self.private = {}
        self.public = {}

    def get_private(self, key, data):
        self.private = json.loads(decrypt(key, data))

    def set_private(self, key):
        return encrypt(key, json.dumps(self.private))