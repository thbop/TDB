from ..utils.encryption import encrypt, decrypt
import json
from copy import copy

class BaseObj:
    def __init__(self):
        self.private = {}
        self._encrypted = False

        self.public = {}

    def load(self, i):
        self.private = i['private']
        self.public = i['public']
    
    def save(self):
        return {
            'private': self.private,
            'public': self.public
        }

    def get_private(self, key):
        if self._encrypted:
            raw_data = decrypt(key, self.private)
            try:
                self.private = json.loads(raw_data)

                self._encrypted = False
                return True
            
            except json.decoder.JSONDecodeError:
                return False
            


    def set_private(self, key):
        if not self._encrypted:
            self.private = encrypt(key, json.dumps(self.private))
            self._encrypted = True
    
    def copy(self):
        return copy(self)