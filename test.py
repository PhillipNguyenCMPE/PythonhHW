from test import double
from test import timestamp
def double(func):
    func()
    print('''Let's try again!''')
    func()
def timestamp(func):
    time.ctime()
    func()
