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





input_List = []
input_List.append(int(input("Enter a number: ")))

while True:
    b = input("Do you want to input more: ")
    if b == 'yes':
        input_List.append(int(input("Enter a number: ")))
    elif b == 'no':
        input_List.sort(reverse=True)
        break

print(input_List)

num = int(input("Enter a number: "))


if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

cities = ["Istabul", "Tokyo", "Helsinki", "Sydney", "New York", "Dubai", "Bern", "Cairo"]

for city in cities:
    print(city)

