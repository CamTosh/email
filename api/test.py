
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

import stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

a = stripe.Subscription.retrieve("sub_GRvgniD3XRpkuv")
print(str(a))