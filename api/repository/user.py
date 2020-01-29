from . import MongoRepository
import bcrypt
from app import mongo
from bson.objectid import ObjectId
from base64 import b64encode, b64decode
from datetime import datetime


class UserRepository(MongoRepository):

    def __init__(self):
        self.collection = 'users'
        super(MongoRepository, self).__init__()

    def addUser(self, user):
        user["created_at"] = datetime.now()
        user['password'] = bcrypt.hashpw(user['password'], bcrypt.gensalt())
        return self.add(user)

    def updateUser(self, userId, data):
        if data['password']:
            print(str('Update password of: ' + userId))
            data['password'] = str(data['password'] ).encode('utf8')
            data['password'] = bcrypt.hashpw(data['password'], bcrypt.gensalt())

        self.update(userId, data)

    def isUserExist(self, mail):
        try:
            return len(mongo.db[self.collection].find_one({'mail': mail})) > 0
        except Exception as e:
            return False
        
    def isApiKeyExist(self, apiKey):
        try:
            return len(mongo.db[self.collection].find_one({'api_key': apiKey})) > 0
        except Exception as e:
            return False
        

    def getUserWithMail(self, mail):
        user = mongo.db[self.collection].find_one({'mail': mail})
        return user

    def getUser(self, id):
        user = self.get(id)
        user.pop('password')

        user['id'] = str(user['_id'])
        user.pop('_id')

        return user

    def isLoginValid(self, mail, password):
        user = self.getUserWithMail(mail)
        
        if bcrypt.checkpw(password.encode('utf8'), user["password"]):
            return user
        else:
            return False
