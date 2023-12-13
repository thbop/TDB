from .base import *

class UserHandler(BaseHandler):
    def __init__(self, db, key, user_obj):
        super().__init__(db, key, user_obj)