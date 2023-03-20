from test import test
def double(func):
    func()
    print('''Let's try again!''')
    func()
def timestamp(func):
    time.ctime()
    func()
