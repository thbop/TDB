
class BaseHandler:
    def __init__(self, db, key, base_obj):
        self.db = db
        self.key = key
        self.base_obj = base_obj
    
    def load(self):
        try:
            if isinstance(self.db.data[self.key], dict):
                self.objects = {}
                for k, i in self.db.data[self.key].items():
                    obj = self.base_obj.copy()
                    obj.load(i)
                    self.objects[k] = obj
            elif isinstance(self.db.data[self.key], list):
                pass
            else:
                raise ValueError('Item must be either a list or a dict')
        except KeyError:
            raise KeyError(f'The key "{self.key}" does not exist in the database, either remove this handler or create the key')
    
    