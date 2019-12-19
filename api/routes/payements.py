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


@routes.route('/payement/charge', methods=['POST'])
@jwt_required
def charge():
	print(str(request.json))
    # creator = userRepository.getUser(get_jwt_identity())
    # if creator == False:
    #     return jsonify({"error": "user doesn't exist"})