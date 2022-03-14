# PRIMARY MODULE

# import helper_module
from helper_module import add

def main():
    # helper_module.say_hello()
    
    number1 = 2
    number2 = 3

    result = add(number1, number2)

    print(result)

my_string = 'cat'

# __name__ refers to this file from the point of
# origin of the file that was executed in the terminal
# print(__name__)



if __name__ == '__main__':
    main()