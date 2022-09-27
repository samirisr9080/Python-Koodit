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


print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)



largest = None
smallest = None
while True:
num = input("Enter a number: ")
if num == "done":
break
try:
n = int(num)
if largest is None or n > largest:
largest = n
elif smallest is None or n < smallest:
smallest = n
except Exception:
print("Invalid input")
continue

print("Maximum is", largest)
print("Minimum is", smallest)









username_password = "python rules"

guess = ""

while guess != username_password:
    guess = input("Enter username and password")

    print("Welcome")

    print("Input your height: ")
    h_ft = int(input("Feet: "))
    h_inch = int(input("Inches: "))

    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)

    print("Your height is : %d cm." % h_cm)

