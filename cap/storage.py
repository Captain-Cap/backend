from itertools import count
from typing import List

from cap.errors import NotFoundError
from cap.factory import BalloonStorage
from cap.schemas import CorrectBalloon


class FakeBalloonsStorage(BalloonStorage):
    name = 'balloons'

    def __init__(self):
        self.storage = {}
        self.last_id = count(1)

    def add(self, balloon: CorrectBalloon) -> CorrectBalloon:
        balloon.uid = next(self.last_id)
        self.storage[balloon.uid] = balloon
        return balloon

    def delete(self, uid) -> None:
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f'reason: balloon id {uid} not found')
        self.storage.pop(uid)

    def update(self, balloon: CorrectBalloon) -> CorrectBalloon:
        if balloon.uid not in self.storage:
            raise NotFoundError(self.name, f'reason: balloon id {balloon.uid} not found')
        self.storage[balloon.uid] = balloon
        return balloon

    def get_balloon_by_id(self, uid) -> CorrectBalloon:
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f'reason: balloon id {uid} not found')
        return self.storage[uid]

    def get_all(self) -> List[CorrectBalloon]:
        return self.storage.values()
