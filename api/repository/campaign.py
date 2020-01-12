from . import MongoRepository
import bcrypt
from app import mongo
from bson.objectid import ObjectId


class CampaignRepository(MongoRepository):

    def __init__(self):
        self.collection = 'campaigns'
        super(MongoRepository, self).__init__()

    def getCampaigns(self, userId):
        campaigns = mongo.db[self.collection].find({'creator': userId})
        result = []
        for campaign in campaigns:
            campaign['id'] = str(campaign['_id'])
            campaign.pop('_id')
            campaign['emails'] = len(campaign['emails'])
            result.append(campaign)

        return result


    def getCampaign(self, userId, cmpgnId):
        campaign = mongo.db[self.collection].find_one({'_id': ObjectId(cmpgnId)})
        if campaign['creator'] != userId:
            return None

        campaign['id'] = str(campaign['_id'])
        campaign.pop('_id')

        return campaign

    def isExist(self, site):
        try:
            return len(mongo.db[self.collection].find_one({'site': site})) > 0
        except Exception as e:
            return False

    def getEmail(self, userId, cmpgnId, fromPager, perPage):
        
        campaign = mongo.db[self.collection].find_one({'_id': ObjectId(cmpgnId)})
        if campaign['creator'] != userId:
            return None

        return mongo.db[self.collection]\
            .find_one({'_id': ObjectId(cmpgnId), 'creator': userId}, {'emails': {'$slice': [fromPager, perPage]}})
