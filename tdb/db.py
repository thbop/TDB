from .handlers import *
from .obj import *
from .utils import *

class Database:
    def __init__(self, filename):
        self.file = TFile(filename)
        try:
            self.load()
        except FileNotFoundError:
            self.data = {}
            self.file.write_json(self.data)
        
        self.handlers = []
    
    def load(self):
        self.data = self.file.read_json()

    def include(self, handler):
        self.handlers.append(handler)

    def save(self):
        for h in self.handlers:
            h.save()
        self.file.write_json(self.data)