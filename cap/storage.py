import logging
from cap.errors import ConflictError, NotFoundError

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class BalloonsStorage:
    name = 'balloons'

    def __init__(self):
        self.storage = {}


    def add(self, balloon):
        uid = balloon['id']
        if self.storage.get(uid):
            logger.error(f"trying to add an existing id {uid}")
            raise ConflictError(self.name, f"reason: id {uid} already exists")
        self.storage[uid] = balloon


    def delete(self, uid):
        if not self.storage.get(uid):
            logger.error(f"trying to delete a non-existent id {uid}")
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        del self.storage[uid]


    def update(self, balloon):
        uid = balloon['id']
        if not self.storage.get(uid):
            logger.error(f"trying to change a non-existent id {uid}")
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        self.storage[uid] = balloon


    def get_balloon_by_id(self, uid):
        if not self.storage.get(uid):
            logger.error(f"calling a non-existent id {uid}")
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        return self.storage[uid]


    def get_all(self):
        return self.storage