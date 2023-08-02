import tdb

class Database(tdb.Database):
    def __init__(self):
        super().__init__('data.tdb')

        self.base_h = tdb.handlers.Base(self)


db = Database()


