from . import MongoRepository
import bcrypt
from app import mongo
from bson.objectid import ObjectId
from base64 import b64encode, b64decode
from datetime import datetime


class SponsorRepository(MongoRepository):

    def __init__(self):
        self.collection = 'sponsors'
        super(MongoRepository, self).__init__()

    def isSponsorExist(self, id):
        try:
            return len(mongo.db[self.collection].find_one({'id': id})) > 0
        except Exception as e:
            return False