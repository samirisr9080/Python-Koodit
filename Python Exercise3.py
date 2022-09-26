zander = float(input("Enter the size of zander by centimeters:"))
if zander<42:
    print("Release the fish back into the lake")




cabinClass = input("enter your cabinclass: ")
cabinClass = cabinClass.lower()
if cabinClass == "lux":
    print("Lux on a balcony cabin of upper deck.")
elif cabinClass == "a":
    print("A on the window cabin above the car deck.")
elif cabinClass == "b":
    print("B om a windowless cabin above the car deck.")
elif cabinClass == "c":
    print("c on the windowless cabin below the car deck.")
else:
    print("Invalid cabin class")






gender = float(input("Enter hemoglobin value:"))


if gender >=134:
    print("Hemoglobin value is low for male but normal for female")
if gender >167:
    print("Hemoglobin value is both  high for male and female")
if gender ==156-167:
    print("Hemoglobin value is normal for male but high for female ")
if gender <117:
    print("Hemogloibn value is both low for male and female")





year = float(input("Enter a year"))

if year%4==0:
    print("This year is a loop year")
else:
    print("This year is not a loop year")


