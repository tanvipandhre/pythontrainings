'''
when you type 'help' you get what all options are there in the game
start, stop the car and quit the game should terminate the program
if you give any other input then it should give output as i dont understand
'''

activity = ""
already_start  = False
already_stop = False
while True:
    activity = input(">")
    activity = activity.upper()
    if activity == 'HELP':
        print('''
start - start the car
stop - stop the car
quit - to exit
        ''')
    elif activity == 'START':
        if not already_start :
            print('Car started.')
            already_start = True
        else:
            print('Car has already started')
    elif activity == 'STOP':
        if not already_stop:
            print('Car stopped.')
            already_stop = True
        else:
           print('Car has already stopped') 
    elif activity == 'QUIT':
        break
    else:
        print("I don't understand.")


