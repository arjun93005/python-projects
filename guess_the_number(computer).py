import random
# the upper limit
y = int(input('Enter a number: '))
def guess(x):
    random_number = random.randint(1, x)
    guessed_number = int(input(f"guess the number from 1 and {x}: "))
    while (guessed_number != random_number):
        if guessed_number < random_number:
            print("the Number you guessed is lower than the right number")
        elif guessed_number > random_number:
            print("the Number you guessed is higher than the right number")
        guessed_number = int(input(f"guess the number from 1 and {x}: "))


    print(f'You guessed right! The number was {random_number}.')

guess(y)