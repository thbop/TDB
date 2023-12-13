from .base import *



class UserObj(BaseObj):
    def __init__(self, uid, username, password):
        # super().__init__()
        self.uid = uid
        self.username = username

        self.public = {
            'uid':self.uid,
            'username':self.username
        }
        self.private = {
            'uid':self.uid
        }
        self._encrypted = False
        self.set_private(password)


