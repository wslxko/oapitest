class SetParameters:
	def __init__(self, case_name, method, token, email, password, confimpwd, result, code, msg, apikey):
		"""
		set parameters
		:param case_name:
		:param method:
		:param token:
		:param email:
		:param password:
		:param confirmpwd:
		:param result:
		:param code:
		:param msg:
		:return:
		"""
		self.case_name = str(case_name)
		self.method = str(method)
		self.token = str(token)
		self.eamil = str(email)
		self.password = str(password)
		self.confimpwd = str(confimpwd)
		self.result = str(result)
		self.code = str(code)
		self.msg = str(msg)
		self.apikey = str(apikey)
		self.response = None
		self.info = None
