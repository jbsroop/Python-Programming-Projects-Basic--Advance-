import random
emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r','p','s')
def get_user_choice():
    while True:
        User = input("Enter the name of the user !")
        user_input = input("Rock,Paper or Scissiors?(r/p/s):").lower()
        if user_input not in choices:
            print('Invalid choice!')
        else:
            return User,user_input

def display_choices(user_input,comp_choice):
    print(f'You chose {emojis[user_input]}')
    print(f'Computer chose {emojis[comp_choice]}')

def determining_winner(User,user_input,comp_choice):
    winning_cases = {('r', 's'), ('p', 'r'), ('s', 'p')}
    if user_input == comp_choice:
        print("The Match is Draw!!")
    elif (user_input, comp_choice) in winning_cases:
        print(User, "Won The Match")
    else:
        print("Computer Won the Match!")

def play_game():   
    User,user_input = get_user_choice()
    while True: 
        comp_choice =random.choice(choices)
        display_choices(user_input,comp_choice)
        determining_winner(User,user_input,comp_choice)
        To_continue = input('Continue? (y/n): ').lower()
        if To_continue == 'n':
            break
play_game()



    





    

