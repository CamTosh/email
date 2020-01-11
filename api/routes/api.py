from flask import jsonify, request
from . import routes
from repository import UserRepository
from app import jsonschema, jwt
from flask_jwt_extended import (
	JWTManager, jwt_required, create_access_token,
	get_jwt_identity
)
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
import os
from base64 import b64encode
from services import Api

userRepository = UserRepository()

@routes.route('/api/token', methods=['GET'])
@jwt_required
def get_api_key():
	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not user['api_key']:
		return jsonify({"error": "No API Key"})

	api = Api()
	apiKey = api.createApiKey(user)
	userRepository.update(user['id'], {'api_key': str(apiKey)})
	return jsonify({'apiKey': apiKey})


@routes.route('/api/token', methods=['POST'])
@jwt_required
def create_api_key():
	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not user['api_key']:
		api = Api()
		apiKey = api.createApiKey(user)
		userRepository.update(user['id'], {'api_key': str(apiKey)})
		return jsonify({'apiKey': apiKey})

	return jsonify({"error": "Api key already exist"})


@routes.route('/api/token', methods=['PUT'])
@jwt_required
def update_api_key():
	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not user['api_key']:
		return jsonify({"error": "no api key"})

	api = Api()
	apiKey = api.createApiKey(user)
	userRepository.update(user['id'], {'api_key': str(apiKey)})

	return jsonify({'apiKey': apiKey})
