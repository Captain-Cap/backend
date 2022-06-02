from cap.errors import ConflictError, NotFoundError


class BalloonsStorage:
    name = 'balloons'

    def __init__(self):
        self.storage = {}


    def add(self, balloon):
        uid = balloon['id']
        if self.storage.get(uid):
            raise ConflictError(self.name, f"reason: id {uid} already exists")
        self.storage[uid] = balloon


    def delete(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        del self.storage[uid]


    def update(self, balloon):
        uid = balloon['id']
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        self.storage[uid] = balloon


    def get_balloon_by_id(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        return self.storage[uid]


    def get_all(self):
        return self.storage