



class BaloonsStorage:

    def __init__(self):
        self.storage = {}


    def add(self, balloon):
        uid = balloon['id']
        if self.storage.get(uid):
            raise ValueError("such id already exists")
        self.storage[uid] = balloon


    def delete(self, uid):
        if not self.storage.get(uid):
            raise KeyError("balloon not found")
        del self.storage[uid]