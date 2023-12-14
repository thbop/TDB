from ..utils.encryption import encrypt, decrypt
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
            dec = decrypt(key, self.private)
            if dec != None:
                self.private = dec
                self._encrypted = False
                return True
            else:
                return False
            
    def set_private(self, key):
        if not self._encrypted:
            self.private = encrypt(key, self.private)
            self._encrypted = True
    
    def copy(self):
        return copy(self)