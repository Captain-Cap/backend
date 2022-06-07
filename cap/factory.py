from abc import ABC, abstractmethod
from typing import List, Union
from cap.models import Balloons
from cap.schemas import CorrectBalloon

class BalloonStorage(ABC):

    @abstractmethod
    def add(self, baloon):
        raise NotImplementedError


    @abstractmethod
    def delete(self, uid):
        raise NotImplementedError


    @abstractmethod
    def update(self, balloon: CorrectBalloon) -> CorrectBalloon:
        raise NotImplementedError


    @abstractmethod
    def get_balloon_by_id(self, uid):
        raise NotImplementedError


    @abstractmethod
    def get_all(self) -> List[Union[Balloons, CorrectBalloon]]:
        raise NotImplementedError
