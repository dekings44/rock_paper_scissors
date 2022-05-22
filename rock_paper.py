

print('Welcome to Rock Paper Scissors Game')

import random



rock = '✊'

scissors = '✌️'

paper = '✋'

choices_emojis = [rock, paper, scissors]

ran_choice = random.randint(0, 2)

user_choice = int(input('Please make a choice. type 0 for rock, 1 for paper or 2 for scissors\n'))

if user_choice >= 3 or user_choice < 0:
    print(f'You typed and invalid number. {user_choice}')
    user_choice = int(input('Please make a choice. type 0 for rock, 1 for paper or 2 for scissors\n'))
else:
    print(choices_emojis[user_choice])
    print('Computer chose')
    print(choices_emojis[ran_choice])


    if user_choice == 0 and ran_choice == 2:
        print('You won')
    elif ran_choice == 0 and user_choice == 2:
        print('You lose')
    elif ran_choice > user_choice:
        print('You lose')
    elif user_choice > ran_choice:
        print('You won')




