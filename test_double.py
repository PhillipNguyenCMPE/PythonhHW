from test import double
def double(func):
    func()
    print('''Let's try again!''')
    func()
