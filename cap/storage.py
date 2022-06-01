



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


    def update(self, balloon):
        uid = balloon['id']
        if not self.storage.get(uid):
            raise ValueError("id does not exist")
        self.storage[uid] = balloon


    def get_balloon_by_id(self, uid):
        if not self.storage.get(uid):
            raise ValueError("balloon not found")
        return self.storage[uid]


    def get_all(self):
        return self.storage