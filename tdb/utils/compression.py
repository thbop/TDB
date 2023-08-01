import gzip
import json


class TFile:
    def __init__(self, base):
        self.base = base
    
    def read(self):
        with gzip.open(self.base, 'rb') as f:
            data = f.read()
        return data.decode()

    def read_json(self):
        '''Returns parsed json as Pythonic data-types'''
        return json.loads(self.read())

    def write(self, data: str):
        with gzip.open(self.base, 'wb') as f:
            f.write(data.encode())

    def write_json(self, data):
        '''Converts any data into json automatically and then writes it to the file.'''
        self.write(json.dumps(data))

if __name__ == '__main__':
    file = TFile('data.tdb')
    file.write_json({'cheese':'puff'})
    print(file.read_json())

