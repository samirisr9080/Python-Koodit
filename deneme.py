import random


def main():
    while True:
        num_dice = int(input('How many dice do you want to roll?'))
        if num_dice < 1 or num_dice > 10:
            print('Enter a number between 1 and 10.')
        else:
            break
    result = roll_dice(num_dice)
    print(f'The total for {num_dice} rolls was {result}.')


def roll_dice(num_dice):
    rolls = 0
    for i in range(1, num_dice + 1):
        print(f'Roll #{i} = {(roll := random.randint(1, 6))}')
        rolls += roll
    return rolls


main()