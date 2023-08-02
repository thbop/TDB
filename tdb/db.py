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
    
    def load(self):
        self.data = self.file.read_json()
    
    def save(self):
        self.file.write_json(self.data)