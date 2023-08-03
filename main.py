import tdb

class Database(tdb.Database):
    def __init__(self):
        super().__init__('data.tdb')

        self.base_h = tdb.handlers.BaseHandler(self, 'games', tdb.obj.BaseObj())
        self.base_h.load()
        print(self.base_h.objects)


db = Database()


