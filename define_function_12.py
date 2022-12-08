def greet_user(firstname, lastname): #name is the parameter
    print(f'Hello World I am {firstname} {lastname}')


print('Before calling funct')
greet_user('Tanvi', 'Pandhre') #Tanvi is the argument.. all they are positional arguments
greet_user(lastname='A',firstname='Gauri') #they are called keyword arguments.. 

print('after calling funct')

# using return statements
def square(num):
    return num * num
number = int(input('enter a num: '))
print(f'square of {number} = {square(number)}  ')