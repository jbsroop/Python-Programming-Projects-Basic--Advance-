import random

emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r','p','s')
while True: 
    User = input("Enter the name of the user !")
    user_input = input("Rock,Paper or Scissiors?(r/p/s):").lower()
    if user_input not in choices:
        print('Invalid choice!')
        continue
    comp_choice = random.choice(choices)
    print(f'You chose {emojis[user_input]}')
    print(f'Computer chose {emojis[comp_choice]}')

    if user_input == 'r' and comp_choice == 'p':
        print("Computer Won the match!")
    elif user_input == 'p'and comp_choice == 'r':
        print(User ,"Won The Match")
    elif user_input == 's' and comp_choice == 'p':
        print(User ,"Won The Match")
    elif user_input == 'p' and comp_choice == 's':
        print("Computer Won the match!")
    elif user_input == 's' and comp_choice == 'r':
        print(User ,"Won The Match")
    elif user_input == 'r' and comp_choice == 's':
        print("Computer Won the match!")
    else:
        print("The Match is draw!!")

To_continue = input('Continue? (y/n): ').lower()

