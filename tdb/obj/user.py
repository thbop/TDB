from .base import *



class UserObj(BaseObj):
    def __init__(self, uid=None, username=None, password=None):
        # super().__init__()

        self.public = {
            'uid':uid,
            'username':username
        }
        self.private = {
            'uid':self.uid
        }
        self._encrypted = False
        self.set_private(password) if password != None else 0

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