
class BaseHandler:
    def __init__(self, db, key, base_obj):
        self.db = db
        self.key = key
        self.base_obj = base_obj

        self.load()

    
    def load(self):
        try:
            if isinstance(self.db.data[self.key], dict):
                self.objects = {}
                for k, i in self.db.data[self.key].items():
                    obj = self.base_obj.copy()
                    obj.load(i)
                    self.objects[k] = obj
            elif isinstance(self.db.data[self.key], list):
                self.objects = []
                for o in self.db.data[self.key]:
                    obj = self.base_obj.copy()
                    obj.load(o)
                    self.objects.append(obj)
            else:
                raise ValueError('Item must be either a list or a dict')
        except KeyError:
            raise KeyError(f'The key "{self.key}" does not exist in the database, either remove this handler or create the key')
    
    def save(self):
        if isinstance(self.objects, dict):
            for k, o in self.objects.items():
                self.db.data[self.key][k] = o.save()

        elif isinstance(self.objects, list):
            self.db.data[self.key] = []
            for o in self.objects:
                self.db.data[self.key].append(o.save())
    
    def set(self, key, obj):
        if isinstance(self.objects, dict):
            self.objects[key] = obj
        else:
            raise TypeError(f'{self.key} is a dictionary. Use add() for lists.')
    def add(self, obj):
        if isinstance(self.objects, list):
            self.objects.append(obj)
        else:
            raise TypeError(f'{self.key} is a list. Use set() for dictionaries.')
        
    def delete(self, key):
        if isinstance(self.objects, dict):
            del self.objects[key]
        else:
            raise TypeError(f'{self.key} is a dictionary. Use remove() for lists.')
    def remove(self, obj):
        if isinstance(self.objects, list):
            self.objects.remove(obj)
        else:
            raise TypeError(f'{self.key} is a list. Use delete() for dictionaries.')
    