import json

class Config:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.config = json.load(f)
    
    def get(self, key):
        return self.config[key]