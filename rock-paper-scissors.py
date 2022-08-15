import random

computer_wins=0
user_wins=0

ROCK='rock'
PAPER='paper'
SCISSORS='scissors'
options=[ROCK,PAPER,SCISSORS]

while True:
    Quit='q'
    user_choice=input('Choose between Rock/Paper/Scissors or type Q to quit ').lower()
    # print(user_choice)

    if user_choice == Quit:
        break
    elif user_choice not in options:
        continue
    else:
        random_choice=random.randint(0, 2)
        computer_choice=options[random_choice]
        # print(computer_choice)

    if user_choice == ROCK and computer_choice == SCISSORS:
        print('You won')
        user_wins += 1         
    elif user_choice == SCISSORS and computer_choice == ROCK:
        print('You won')
        user_wins += 1  
    elif user_choice == SCISSORS and computer_choice == PAPER:
        print('You won')
        user_wins += 1      
    elif user_choice == computer_choice:
        print('Draw')      
    else:
        print('Computer won :(')
        computer_wins += 1

print(f'You won {user_wins} times')            
print(f'Computer won {computer_wins} times')            

