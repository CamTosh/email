
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

# import stripe
# stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# data = stripe.Customer.retrieve("cus_GSMWwZJ5v5iOhk")
# #a = stripe.Subscription.retrieve("sub_GRvgniD3XRpkuv")

# result = []

# for sub in data['subscriptions']['data']:
# 	obj = {
# 		'id': sub['id'],
# 		'end': sub['current_period_end'],
# 		'start': sub['current_period_start'],
# 		'active': sub['items']['data'][0]['plan']['active'],
# 		'interval': sub['items']['data'][0]['plan']['interval'],
# 		'amount': sub['items']['data'][0]['plan']['amount'],
# 		'plan': sub['items']['data'][0]['plan']['nickname'].lower(),
# 	}
# 	result.append(obj)

# print(str(result))

