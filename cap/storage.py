from itertools import count
from cap.errors import ConflictError, NotFoundError
from cap.schemas import CorrectBalloon



class BalloonsStorage:
    name = 'balloons'

    def __init__(self):
        self.storage = {}
        self.last_id = count(1)


    def add(self, balloon):
        balloon = CorrectBalloon(**balloon).dict()
        del balloon['id']
        uid = next(self.last_id)
        if self.storage.get(uid):
            raise ConflictError(self.name, f"reason: id {uid} already exists")
        self.storage[uid] = balloon


    def delete(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        del self.storage[uid]


    def update(self, balloon):
        balloon = CorrectBalloon(id=balloon["id"], **balloon["fields"]).dict()
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