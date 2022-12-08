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
output = ''
for num in phoneno:
    #print(numbers.get(num), end = ' ')
    output += numbers.get(num) + " "

print(f'Output --> {output}')

'''
program to make a sentences w symbols into emojis
'''
message = input('Enter a message:')
words = message.split(' ')
print(words)
emojis = {
    ":)" : "^_^",
    ":(" : "^c^"
}
outputt = ''
for word in words:
    outputt += emojis.get(word, word) + " "
print('emoji output -->  ', outputt)

'''
making a function out of it
'''
def print_emojis(message):
    words = message.split(' ')
    print(words)
    emojis = {
        ":)" : "^_^",
        ":(" : "^c^"
    }
    outputt = ''
    for word in words:
        outputt += emojis.get(word, word) + " "
    return outputt


msg = input('enter msg ')
output_msg = print_emojis(msg)
print(f"we don't worry about i/p n o/p in the method --> {output_msg}")