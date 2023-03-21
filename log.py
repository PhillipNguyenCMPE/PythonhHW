import time
def timestamp(func):
	def wrapper():
		time.ctime()
		func()
	return wrapper

