# dictionary - use {} for a dictionary. keys should be unique
customer = {
    "name" : "Tanvi Pandhre",
    "age" : 24,
    "is_Verified" : True

}
print('To get the value of key --> ',customer["name"])
print('To get the value of key using get method --> ',customer.get("age"))
#see the output when we have no key present in the dict
print('If there is no key --> ', customer.get("birthdate"))
# if we want to set a default value to a key
print('set default value --> ', customer.get("birthdate", "Jan 1 1997"))
# can add new key value pairs

'''
project - take phone no in the form of integers and display output in words
'''
phoneno = input('Phone: ')
numbers = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three'
}
for num in phoneno:
    print(numbers.get(num), end = ' ')
