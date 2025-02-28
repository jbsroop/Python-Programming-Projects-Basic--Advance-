import random
random_num = random.randint(1,100)
while True:
    try:   
        Guess_num = int(input('Guess a number between 1 to 100:'))
        
        if Guess_num > random_num:
            print('Too high!')
        elif Guess_num < random_num:
            print('Too low!')
        else:
            print("Congratulations! You guessed the number")
            break
    except ValueError:
        print('Please give a valid number')
        
