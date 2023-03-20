from log import timestamp
@timestamp
def hi():
	print('hi')
def main():
	hi()
def timestamp(func):
    time.ctime()
    func()

