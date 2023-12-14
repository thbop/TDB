from .base import BaseObj
from ..utils.encryption import encrypt, decrypt
import secrets


class UserObj(BaseObj):
    def __init__(self, uid=None, username=None, password=None):
        # super().__init__()

        self.public = {
            'uid':secrets.token_hex() if uid == None else uid,
            'username':username
        }
        self.private = { # Make token unlock
            'uid':self.uid
        }
        self.token = {
            'uid':self.uid,
            'token': secrets.token_hex()
        } # password is key to unlock this


        self._hidden_token = False
        self._encrypted = False

        
        self.set_private(self.token['token'])
        if password != None:
            self.hide_token(password)

    @property
    def uid(self):
        return self.public['uid']
    @uid.setter
    def uid(self, uid):
        self.public['uid'] = uid
    @property
    def username(self):
        return self.public['username']
    @username.setter
    def username(self, username):
        self.public['username'] = username
    
    def load(self, i):
        super().load()
        self.token = i['token']
    
    def save(self):
        return {
            'private': self.private,
            'public': self.public,
            'token': self.token
        }

    def get_token(self, key): # password
        if self._hidden_token:
            dec = decrypt(key, self.token)
            if dec != None:
                self.token = dec
                self._hidden_token = False
                return True
            else:
                return False

            
    def hide_token(self, key):
        if not self._hidden_token:
            self.token = encrypt(key, self.token)
            self._hidden_token = True

    
    def auth(self, key, token_mode=True): # key = token if token_mode else password
        '''
        Check if decryption and json stuff go well.
        Make sure result is dictionary (it should be anyways once I remove my aes junk).
        Then compare uids.
        '''
        if token_mode:
            if self.get_private(key) and isinstance(self.private, dict) and self.public['uid'] == self.private['uid']:
                self.set_private(key)
                return True
            else:
                return False
        else: # We're using password to unlock token
            rtn = False
            
            if self.get_token(key) and isinstance(self.token, dict) and self.public['uid'] == self.token['uid']:
                self.get_private(self.token['token'])
                rtn = secrets.token_hex()
                self.token['token'] = rtn
                self.set_private(rtn) # Re-encrypt private with new token
                self.hide_token(key)
                return rtn
            else:
                return rtn