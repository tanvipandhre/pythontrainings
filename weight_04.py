# convert weight in pounds to kgs
weight_pounds = float(input("enter weight in pounds "))
weight_kgs = 0.453 * weight_pounds
print("weight in kgs ", weight_kgs)

'''
project - that will take input as weight
take input as L or K for lbs or kgs
convert into vice versa 
like if you take input in kgs then convert it to lbs and show as output
'''

weight = input('enter  weight: ')
unit = input('enter the unit of given weight (L)bs or (K)g')
if unit == 'L' or unit == 'l': #converting lbs to kgs
    weight_kgs = 0.453 * float(weight)
    print(f'You are {weight_kgs} kilos')
elif unit.upper() == 'K': #converting kgs to lbs
    weight_pounds = 2.2 * float(weight)
    print(f'You are {weight_pounds} pounds')

