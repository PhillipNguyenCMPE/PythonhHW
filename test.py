from test import greet
from test import hi
def double(func):
    func()
    print('''Let's try again!''')
    func()
def timestamp(func):
    time.ctime()
    func()
