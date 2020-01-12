
class Pager(object):

	def __init__(self, request):
		try:
			self.page = int(request.args.get('page'))
		except:
			self.page = 0
		try:
			self.perPage = int(request.args.get('per_page'))
			if self.perPage >= 30:
				self.perPage = 30
		except:
			self.perPage = 10
