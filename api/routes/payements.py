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
		'stripe': {
			'monthly': 'plan_GSJSSCSnn80JRK',
			'annualy': 'plan_GWMebS1oanaat3',
		},
		'campaigns': 5,
		'emailsPerCampaign': 5000
	},
	'startup': {
		'stripe': {
			'monthly': 'plan_GSJS49XeJs5fh0',
			'annualy': 'plan_GWMdPRSpaJaGPx',
		},
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

	period = data['period']
	if period not in ['monthly', 'annualy']:
		return jsonify({'error': 'bad period'})

	user = userRepository.getUser(get_jwt_identity())
	if user == False:
		return jsonify({"error": "user doesn't exist"})

	if not user['customer_id']:
		# Create customer on stripe
		print('Create customer for: [{}][{}]'.format(user['mail'], user['id']))
		try:		
			customer = stripe.Customer.create(
				email=user['mail'],
				description="[{}] - {} {}".format(user['id'], user['firstName'], user['lastName']),
				source=data['stripeToken'],
				metadata={
					"id": user['id'],
					"email": user['mail'],
					"firstName": user['firstName'],
					"lastName": user['lastName'],
				},
			)
		except Exception as e:
			print(str(e))
			return jsonify({'error': 'stripe error'})

		customerId = customer.id
		userRepository.update(user['id'], {'customer_id': customerId})
	else:
		# Cancel current subscription
		customerId = user['customer_id']
		
		customerData = stripe.Customer.retrieve(customerId)
		currentSubscription = stripe.Subscription.retrieve(
			customerData['subscriptions']['data'][0].id
		)

		stripe.Subscription.delete(currentSubscription.id)	
	try:
		# Create subscription for plan
		subscription = stripe.Subscription.create(
		  customer=customerId,
		  items=[{
		  	"plan": plans[plan]['stripe'][period]
		  }],
		)

	except Exception as e:
		print(str(e))
		return jsonify({'error': 'stripe error'})

	try:	
		# Persist invoice
		invoice = []
		if 'invoice' in user.keys():
			invoice = user['invoice']

		invoice.append({
			'created_at': datetime.now(),
			'plan': plan,
			'period': period,
			'price': subscription.plan.amount,
			'currency': subscription.plan.currency,
			'id': subscription.id,
			'start': subscription.current_period_start,
			'end': subscription.current_period_end,
		})

		userRepository.update(user['id'], {
			'plan': {
				'id': plan,
				'period': period,
				'campaigns': plans[plan]['campaigns'],
				'emailsPerCampaign': plans[plan]['emailsPerCampaign']
			},
			'invoice': invoice
		})

		return jsonify(invoice)
	except Exception as e:
		print(str(e))
		return jsonify({'error': 'stripe error'})