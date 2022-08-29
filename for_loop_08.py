#printing each character
for item in 'Python':
    print(item)

#print list of items
for i in ['Mosh', 'John', 'Tanvi']:
    print(i)

#range function
print('using range function')
for ii in range(10):
    print(ii)

# select a certain range of numbers
print('certain range')
for i3 in range(5, 10):
    print(i3)

# to take more than one step
print('take more than one step')
for i4 in range(5, 10, 2):
    print(i4)

'''
shopping cart - add all prices
'''

prices = [10, 20 , 30, 45, 55]
sum = 0
for item in prices:
    sum += item
print('Total cost: ', sum)

'''
nested loops
'''
print('nested loop coordinates')
count = 1
for x in range(5):
    for y in range(3):
        print(f'({x}, {y}) --> {count}')
        count += 1

'''
print a 'F' using single loop
'''
numbers = [5, 2, 5, 2, 2]
for y in numbers:
    print('*' * y) #in python we can multiply string with integer to make it repeat
print()


'''
print a 'F' using nested loop
'''
nums = [5, 2, 5, 2, 2]
for num in nums:
    output = ''
    for count in range(num):
        output += 'x'
    print(output)
print()

'''
print a 'L' using nested loop
'''

numbs = [2, 2, 2, 5, 5]
for numb in numbs:
    otp = ''
    for count in range(numb):
        otp += 'x'
    print(otp)


'''
operations
'''
names = ['Tanvi', 'Gauri', 'Yashna']
print(names[1:])
names[0] = 'Yogita'
print(names)

'''
largest number in the list
'''
nums = [10, 20, 50, 15, 40]
temp = nums[0]
for i in nums:
    if i > temp:
        temp = i
    
print('largest num -->', temp)