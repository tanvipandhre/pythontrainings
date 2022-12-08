try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('You cannot print by zero.')

