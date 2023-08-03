from ..utils.encryption import encrypt, decrypt
import json
from copy import copy

class BaseObj:
    def __init__(self):
        self.private = {}
        self._encrypted = True

        self.public = {}

    def load(self, i):
        self.private = i['private']
        self.public = i['public']

    def get_private(self, key, data):
        if not self._encrypted:
            self.private = json.loads(decrypt(key, data))
            self._encrypted = False

    def set_private(self, key):
        if self._encrypted:
            self.private = encrypt(key, json.dumps(self.private))
            self._encrypted = True
    
    def copy(self):
        return copy(self)