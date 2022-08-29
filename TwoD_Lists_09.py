#2D lists are used to make 3D matrix is maths
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
    print()

'''
list methods
'''
numbers = [5, 2, 7, 4, 1]
numbers.append(9) #append adds a number to the list
print('Append method -->', numbers)

# to add number somewhere in the middle of the list
nums = [4, 3, 7, 9, 10]
nums.insert(2, 8) # insert takes 2 params index and int to be inserted
print('Inserted list -->', nums)

#remove the item
nums.remove(7)
print('Remove int ---> ',nums)

#to clear all the element in the list
nums.clear()
print('Clear all elements in the list', nums)

#removes last element from the list
numss = [2, 3, 4, 9, 7]
numss.pop()
print('Removes last element from the list',numss)

#finds index of the element
index = numss.index(4)
print('index of a element --> ', index)

'''
#if some element is not present and we use index method
ind = numss.index(50)
print('Throw error', ind)
'''

#if some element is not found in operator returns false
print("is it there? -->", 30 in numss)

#count the number of elements
numss.append(9)
print('Number of elements', numss.count(9))

# sort the numbers
numss.sort()
print('Sorted the nums', numss)

#reverse the numbers
numss.reverse()
print('Reverse the nums', numss)

#to copy list to another
nums2 = numss.copy()
print('Copy of nums', nums2)

'''
remove duplicates from the list
'''
nums3 = [2, 7, 6, 7, 5, 7]
nums3.sort()
for num in nums3:
    #size = len(nums3)
    ind = nums3.index(num)
    ind = ind+1
    temp = nums3[ind]
    if temp <= num:
        nums3.remove(temp)
print('after removing duplicates --> ',nums3)

'''
remove duplicates from the list using an empty array
'''
nums4 = [2, 7, 6, 7, 5, 7]
unique = []
for num in nums4:
    if num not in unique:
        unique.append(num)
print(unique)



