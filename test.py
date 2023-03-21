from double import double
from log import timestamp

@timestamp
def greet():
    print('Hello World!')
def main():
    greet()
main()

@timestamp
def hi():
    print('hi')
    
def main():
    hi()
main() 
          
          
