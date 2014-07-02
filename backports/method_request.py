try:
	import urllib.request as request
except ImportError:
	# Python 2
	import urllib2 as request

class Request(request.Request):
	method = None

	def __init__(self, *args, **kwargs):
		"""
		Construct a Request. Usage is the same as for
		`urllib.request.Request` except it also takes an optional `method`
		keyword argument. If supplied, `method` will be used instead of
		the default.
		"""
		method = kwargs.pop('method', self.method)
		request.Request.__init__(self, *args, **kwargs)
		# write the method after __init__ as Python 3.3 overrides the value
		self.method = method

	def get_method(self):
		return getattr(self, 'method') or request.Request.get_method(self)
