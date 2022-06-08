from abc import ABC, abstractmethod
from typing import List

from cap.schemas import CorrectBalloon


class BalloonStorage(ABC):

    @abstractmethod
    def add(self, baloon: CorrectBalloon) -> CorrectBalloon:
        raise NotImplementedError

    @abstractmethod
    def delete(self, uid: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, balloon: CorrectBalloon) -> CorrectBalloon:
        raise NotImplementedError

    @abstractmethod
    def get_balloon_by_id(self, uid: int) -> CorrectBalloon:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[CorrectBalloon]:
        raise NotImplementedError
