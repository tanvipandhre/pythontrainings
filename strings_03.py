course = "learn dsa properly"
#methods of string --  
print(course.upper()) #converts to upper case
print(course.find('d')) #returns first index of the char or word #it is case sensitive 
print(course.replace('dsa', 'ds algo')) # replaces the chars
print('ds' in course) #in operator returns boolean check if the word is present in the object(string)
print("Taking Mosh's Python course") # for setting up single quotes in between, put double quotes on outer part
print('Python for "Begineers"') # for setting up double quotes
print(''' 
Hi Tanvi
How is New york
take care
''') # use triple quote for multi line
print("First char of course ", course[0])
print("Last char of course ", course[-1]) # this is rare, to take last char
print("first 3 chars ",course[0:3]) 
print("first 4 chars ",course[:4]) # it assumes 0 start to 3rd char
print("all chars -->",course[:]) # all chars
print("all chars from 1to -1 -->",course[1:-1]) # all chars except first and last

#formatted string
# you have to print Tanvi [Pandhre] is a coder
firstname = 'Tanvi'
lastname = 'Pandhre'
message = firstname + ' [' + lastname + '] is a coder' #this is concatenation
print('message --> ', message) 
formattedMessage =  f'{firstname} [{lastname}] is a coder' # formatted string begins with f'' and variable name is kept in {}
print('formattedMessage --> ', formattedMessage) 
print('length of the string = ', len(firstname))   #len function to find string length, also give size of arraylist


