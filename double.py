from double import double
@timestamp
def greet():
	print('Hello World!')
def main():
	greet()
def double(func):
    func()
    print('''Let's try again!''')
    func()
main()
