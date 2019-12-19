from flask import jsonify, request
from . import routes
from repository import UserRepository
from app import jsonschema, jwt
from bson import ObjectId
from flask_jwt_extended import (
	JWTManager, jwt_required, create_access_token,
	get_jwt_identity
)
import datetime

userRepository = UserRepository()


@routes.route('/user', methods=['GET'])
@jwt_required
def user_info():
	return userRepository.getUser(get_jwt_identity())


@routes.route('/user', methods=['POST'])
@jsonschema.validate('user', 'create')
def user_create():
	mail = str(request.json['mail'])

	user = userRepository.isUserExist(mail)
	if user != False:
		return jsonify({"error": "User already exist"})
	
	res = userRepository.addUser({
		"mail": mail,
		"password": str(request.json['password']).encode('utf8'),
		"instagram_account": request.json['instagram_account'],
		"instagram_password": str(request.json['password']).encode('utf8'),
		"role": "user",
	})
	expires = datetime.timedelta(days=365)
	return jsonify({"bearer": create_access_token(str(res.inserted_id), expires_delta=expires)})


@routes.route('/user', methods=['PUT'])
@jsonschema.validate('user', 'update')
@jwt_required
def user_update():
	user = userRepository.getUser(get_jwt_identity())
	if not user:
		return jsonify({"error": "User not exist"})

	userRepository.update(user['id'], request.json)
	return jsonify(True)


@routes.route('/user', methods=['DELETE'])
@jwt_required
def user_delete():
	user = userRepository.getUser(get_jwt_identity())
	if not user:
		return jsonify({"error": "User not exist"})
   
	userRepository.remove(user['id'])
	return jsonify(True)


@routes.route('/login', methods=['POST'])
def login():
	user = userRepository.isLoginValid(
		request.json['mail'], 
		str(request.json['password'])
	)
	
	if not user:
		return jsonify({"error": "User not exist"})

	expires = datetime.timedelta(days=365)
	return jsonify({"bearer": create_access_token(str(user['_id']), expires_delta=expires)})
