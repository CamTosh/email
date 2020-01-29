from flask import jsonify, request
from . import routes
from repository import UserRepository
from app import jsonschema, jwt
from flask_jwt_extended import (
	JWTManager, jwt_required, create_access_token,
	get_jwt_identity
)
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
from services import ApiService

userRepository = UserRepository()

# Crud API Token

@routes.route('/api/token', methods=['GET'])
@jwt_required
def get_api_key():
	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not 'api_key' in user:
		return jsonify({"error": "No API Key"})

	return jsonify({'apiKey': user['api_key']})


@routes.route('/api/token', methods=['POST'])
@jwt_required
def create_api_key():
	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not 'api_key' in user:
		api = ApiService()
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

	if not 'api_key' in user:
		return jsonify({"error": "no api key"})

	api = ApiService()
	apiKey = api.createApiKey(user)
	userRepository.update(user['id'], {'api_key': str(apiKey)})

	return jsonify({'apiKey': apiKey})



@routes.route('/api/test', methods=['GET'])
def test_api():
	if not request.headers.get('api_key'):
		return jsonify({'error': 'Header Api_key is not defined'})

	isApiKeyExist = userRepository.isApiKeyExist(request.headers.get('api_key'))
	
	if not isApiKeyExist:
		return jsonify({'error': 'This api key does not exist'})

	return jsonify({'staus': True})
