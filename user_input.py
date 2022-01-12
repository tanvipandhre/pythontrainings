name = input('Enter name')
print('You entered',name)

#input() takes default string 
a = int(input('Enter a'))
b = int(input('Enter b'))
c = a*b
print(c)

#program to ask user marks in eng, maths, science
marks_eng = int(input('Enter marks scored in english'))
marks_math = int(input('Enter marks scored in math'))
marks_science = int(input('Enter marks scored in science'))
marks_avg = (marks_eng+marks_math+marks_science)/3
print('Avg marks are',marks_avg)