from log import timestamp
def timestamp(func):
	def wrapper():
		print(time.ctime())
		func()
	return wrapper

