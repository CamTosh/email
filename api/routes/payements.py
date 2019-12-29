from flask import jsonify, request
from . import routes
from repository import UserRepository, CampaignRepository
from app import jsonschema, jwt
from bson import ObjectId
from flask_jwt_extended import (
	JWTManager, jwt_required, create_access_token,
	get_jwt_identity
)
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

import stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

userRepository = UserRepository()
campaignRepository = CampaignRepository()

plans = {
	'indie': {
		'stripe': 'plan_GP0jHMr6I8Ri6E',
		'campaigns': 5,
		'emailsPerCampaign': 5000
	},
	'startup': {
		'stripe': 'plan_GP0lG51Rl7Lsq7',
		'campaigns': 10,
		'emailsPerCampaign': 10000
	}
}


@routes.route('/purchase', methods=['POST'])
@jwt_required
def charge():
	data = request.json
	plan = data['plan'].lower()
	
	if plan not in plans.keys():
		return jsonify({'error': 'bad plan'})

	if not data['stripeToken']:
		return jsonify({'error': 'bad stripe token'})

	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not user['customer_id']:
		print('Create customer for: [' + user['mail'] + '][' + user['id'] + ']')
		customer = stripe.Customer.create(
			description=user['mail'],
			source=data['stripeToken'],
			metadata={
				"id": user['id'],
				"mail": user['mail'],
				"firstName": user['firstName'],
				"lastName": user['lastName'],
			},
		)
		userRepository.update(user['id'], {'customer_id': customer.id})
		customer_id = customer.id
	else:
		customer_id = user['customer_id']

	try:	
		subscription = stripe.Subscription.create(
		  customer=customer_id,
		  items=[{
		  	"plan": plans[plan]['stripe']
		  }],
		)

		invoice = []
		if user['invoice']:
			invoice = user['invoice']

		invoice.append({
			'created_at': datetime.now(),
			'plan': plan,
			'price': subscription.plan.amount,
			'currency': subscription.plan.currency,
			'id': subscription.id,
			'start': subscription.current_period_start,
			'end': subscription.current_period_end,
		})

		userRepository.update(user['id'], {
			'plan': {
				'id': plan,
				'campaigns': plans[plan]['campaigns'],
				'emailsPerCampaign': plans[plan]['emailsPerCampaign']
			},
			'invoice': invoice
		})

		return jsonify(True)
	except Exception as e:
		print(str(e))
		return jsonify({'error': 'stripe error'})