def foo():
    print('I\'m a function from lib')


variable1 = 100
variable2 = 'abcdef'


print(f'__name__ in lib is {__name__}')

# print('Inside library')
# foo()

if __name__ == '__main__':

    print('Inside library')
    foo()
