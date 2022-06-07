from typing import List
from itertools import count
from cap.errors import NotFoundError
from cap.schemas import CorrectBalloon



class FakeBalloonsStorage:
    name = 'balloons'

    def __init__(self):
        self.storage = {}
        self.last_id = count(1)


    def add(self, balloon: CorrectBalloon) -> CorrectBalloon:
        balloon.uid = next(self.last_id)
        self.storage[balloon.uid] = balloon
        return balloon


    def delete(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        del self.storage[uid]


    def update(self, balloon: CorrectBalloon) -> CorrectBalloon:
        if balloon.uid not in self.storage:
            raise NotFoundError(self.name, f"reason: balloon id {balloon.uid} not found")
        self.storage[balloon.uid] = balloon
        return balloon


    def get_balloon_by_id(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        return self.storage[uid]


    def get_all(self) -> List[CorrectBalloon]:
        return [balloon for balloon in self.storage.values()]