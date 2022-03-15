from random import randint
from time import sleep

diceType = int(input('Which dice would you like to roll? [6,10,12,20,100]: '))

while True:
    if diceType == 6 or diceType == 10 or diceType == 12 or diceType == 20 or diceType == 100:
        dice = randint(1, diceType)
        print('Rolling dice...')
        for c in range(0, 3):
            sleep(0.5)
            print('.')
        print(f'The D{diceType} was {dice}')
        break
    else:
        print('Please, inform a valid number')
        diceType = int(input('Which dice would you like to roll? [6,10,12,20,100]: '))