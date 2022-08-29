'''
print a tree with increasing number of dollar
'''
i = 1
while i <= 5:
    print('$' * i)
    i += 1
print('done')

'''
Guessing game - guess a number
give them 3 chances to guess
'''
secret_num = 9
i = 1
while i<=3:
    guessed_num = int(input('Guess: '))
    i += 1
    if secret_num == guessed_num:
        print('You win.. you guessed it correct')
        break
    
  
    
else: # while statement also has else part
        print("You loose.. run the program again to play again")





