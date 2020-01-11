import requests

class Email(object):
	
	def validateEmail(self, email):
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