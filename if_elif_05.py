'''
if hot --> print hot day , drink water
if cold --> cold day, wear warm clothes
else --> lovely day
'''
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('wear warm clothes')
else:
    print("It's a lovely day")


'''
price of house is 1million
if buyer has good credit
put down 10 %
else put down 20%
print the down payment
'''
price = 1000000
credit = True
if credit:
    down_payment =  0.1 * price
else:
    down_payment =  0.2 * price
print(f'Down payment : ${down_payment}')

'''
if applicat has high inome and good credit 
eligible for loan

if applicant has high income and no criminal record .. 
eligible for loan
'''
has_high_income = True
has_good_credit = False
has_criminal_record = False
if has_high_income and has_good_credit:
    print('eligible for loan')
elif has_high_income and not has_criminal_record:
    print('eligible for loan 2')

'''
if temp > 30 
it's a hot day
else if temp < 10
it's a cold day
else
it's neither hot nor cold
'''

temp = 8
if temp > 30:
    print(" it's a hot day.")
elif temp < 10:
    print(" it's a cold day.")
else:
    print("it's neither hot nor cold.")

'''
if name < 3 chars long
name must be atlest 3 chars
elif name > 50 chars
name len can be maximum 50 chars
else 
name looks good
'''

name = input('Enter a name')
if len(name) < 3:
    print('name must be atlest 3 chars')
elif len(name) > 50:
    print('name len can be maximum 50 chars')
else:
    print('name looks good')

