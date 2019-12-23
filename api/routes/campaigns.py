from flask import jsonify, request
from . import routes
from repository import UserRepository, CampaignRepository
from app import jsonschema, jwt
from bson import ObjectId
from flask_jwt_extended import (
	JWTManager, jwt_required, create_access_token,
	get_jwt_identity
)

userRepository = UserRepository()
campaignRepository = CampaignRepository()
from datetime import datetime


@routes.route('/campaign', methods=['GET'])
@jwt_required
def campaign_list():
    user = userRepository.getUser(get_jwt_identity())
    campaigns = campaignRepository.getCampaigns(user['id'])
    return jsonify({'campaigns': campaigns})


@routes.route('/campaign/<id>', methods=['GET'])
@jwt_required
def campaign_info(id):
    user = userRepository.getUser(get_jwt_identity())
    if user == False:
        return jsonify({"error": "user doesn't exist"})
    campaign = campaignRepository.getCampaign(user['id'], id)

    campaign['total'] = len(campaign['emails'])
    campaign['emails'] = campaign['emails'][0:user['plan']['emailsPerCampaign']]

    return jsonify(campaign)


@routes.route('/campaign', methods=['POST'])
@jsonschema.validate('campaign', 'create')
@jwt_required
def campaign_create():
    creator = userRepository.getUser(get_jwt_identity())
    if creator == False:
        return jsonify({"error": "user doesn't exist"})
    
    campaign = campaignRepository.isExist(request.json['site'])
    if campaign != False:
        return jsonify({"error": "campaign already exist"})

    campaignsOfUser = len(campaignRepository.getCampaigns(creator['id'])) +1
    if creator['plan']['campaigns'] < campaignsOfUser:
        return jsonify({'error': 'You have reached limit'})

    res = campaignRepository.add({
        "creator": creator['id'],
        "name": request.json['name'],
        "site": request.json['site'],
        "created_at": datetime.now(),
        "emails": []
    })

    return jsonify({'id': str(res.inserted_id)})


@routes.route('/email', methods=['POST'])
@jsonschema.validate('email', 'create')
def add_email():
    campaign = campaignRepository.get(request.json['campaign'])
    if campaign == False:
        return jsonify({"error": "campaign not exist"})
    
    origin = str(request.headers.get('Origin'))
    if origin != campaign['site']:
        print(str({"origin": origin, "site": campaign['site']}))
        return jsonify({'error': 'bad site'})

    email = str(request.json['email'])
    if email in [e['email'] for e in campaign['emails']]:
        return jsonify({'error': 'already added'})

    campaign['emails'].append({"email": email, "created_at": datetime.now()})
    res = campaignRepository.update(str(campaign['_id']), {
        "emails": campaign['emails']
    })

    return jsonify(True)

@routes.route('/campaign/<id>', methods=['DELETE'])
@jwt_required
def campaign_delete(id):
    creator = userRepository.getUser(get_jwt_identity())
    if creator == False:
        return jsonify({"error": "user doesn't exist"})

    campaign = campaignRepository.get(ObjectId(id))

    if campaign == False:
        return jsonify({"error": "campaign don't exist"})

    if campaign['creator'] == creator['id']:
        campaignRepository.remove(id)
        return jsonify(True)

    return jsonify({'error': "Error"})