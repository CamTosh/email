import json 

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
"""
import stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

data = stripe.Customer.retrieve("cus_GSgKyKUcpjdyHZ")
#a = stripe.Subscription.retrieve("sub_GRvgniD3XRpkuv")

result = []

for sub in data['subscriptions']['data']:
	obj = {
		'id': sub['id'],
		'end': sub['current_period_end'],
		'start': sub['current_period_start'],
		'active': sub['items']['data'][0]['plan']['active'],
		'interval': sub['items']['data'][0]['plan']['interval'],
		'amount': sub['items']['data'][0]['plan']['amount'],
		'plan': sub['items']['data'][0]['plan']['nickname'].lower(),
	}
	result.append(obj)

print(json.dumps(result))
"""
import re
import requests

def emailIsValid(email):
	url = 'https://mailtester.com/testmail.php'

	formdata = {
		'lang': 'en',
		'email': email
	}
	r = requests.post(url, data=formdata)
	"""
	regex = r"value=\"(\w+.@\w+.\.\w+.)\""
	matches = re.search(regex, r.text)
	email = matches.group(1)
	"""
	if 'E-mail address is valid' in r.text:
		return {
			"status": True,
			"valid": True,
			"email": email
		}
	elif 'E-mail address does not exist on this server' in r.text:
		return {
			"status": True,
			"valid": False,
			"email": email
		}
	elif "Server doesn't allow e-mail address verification" in r.text:
		return {
			"status": None,
			"valid": None,
			"email": email
		}
	else:
		return {
			"status": False,
			"valid": None,
			"email": email
		}
if __name__ == '__main__':
	
	print(json.dumps(emailIsValid('281008@supinfo.com')))
	print(json.dumps(emailIsValid('k,om281008@supinfo.com')))
	print(json.dumps(emailIsValid('tochecamille@gmail.com')))
	print(json.dumps(emailIsValid('tochecamillerenzbug@gmail.com')))
