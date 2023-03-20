from test import double
from test import log
def double(func):
    func()
    print('''Let's try again!''')
    func()
def timestamp(func):
    time.ctime()
    func()
