n = 1
m = 1000

div = [3]

while(n<=m):
    if n == 4:
        n += 1
        continue
    if n%div[0]==0:
        print(n, 'the number is divisible by 3')

    else:
        print(n, 'is not divisble by 3')
    n += 1





username_password = "python rules"

guess = ""

while guess != username_password:
    guess = input("Enter username and password")

    print("Welcome")

