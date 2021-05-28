from random import randint

easy_attempts = 10
hard_attempts = 5
computer = randint(1, 100)
end_game = False

print('*-*- Welcome to the Number Guessing Game! *-*-'.upper())
print('\nI´m thinking of a number between 1 and 100.\n')
user_choice = str(input('Choose a difficulty. Type "easy" or "hard": ')).lower()

while not end_game:
    if user_choice == 'easy':
        print(f'You have {easy_attempts} attempts remaining to guess the number.')
        user_guess = int(input('Make a guess: '))
        if user_guess == computer:
            print('Congratulations! You win')
            end_game = True
        else:
            if easy_attempts == 1:
                end_game = True
                print(f'\nYou Lost it. The secret number was {computer}')
                break
        if user_guess > computer:
            print('Too high!\nGuess again!\n')
            easy_attempts -= 1
        elif user_guess < computer:
            print('Too low!\nGuess again!\n')
            easy_attempts -= 1
    elif user_choice == 'hard':
        print(f'You have {hard_attempts} attempts remaining to guess the number.')
        user_guess = int(input('Make a guess: '))
        if user_guess == computer:
            print('Congratulations! You win')
            end_game = True
        else:
            if hard_attempts == 1:
                end_game = True
                print(f'\nYou Lost it. The secret number was {computer}')
                break
        if user_guess > computer:
            print('Too high!\nGuess again!\n')
            hard_attempts -= 1
        elif user_guess < computer:
            print('Too low!\nGuess again!\n')
            hard_attempts -= 1
