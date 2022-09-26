user = input("Enter your name:")
print("Nice to meet you," + user + "!")


import math
radius = float(input ("Enter the radius of the circle : "))

area = math.pi * radius * radius
print("Area of the Circle is : {0}".format(area))

print("Enter Length of Rectangle: ")
l = int(input())
print("Enter Breadth of Rectangle: ")
b = int(input())
p = 2*(l+b)
print("\nPerimeter = ", p)

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
sum=a+b+c
product = a*b*c
average=(a+b+c)/3
print ("The Product is: ",product)
print("The sum is:" ,sum)
print("The average is:" ,average)

import random


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res
num = 3
start = 0
end = 9
print(Rand(start, end, num))


import random


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res
num = 4
start = 1
end = 6
print(Rand(start, end, num))