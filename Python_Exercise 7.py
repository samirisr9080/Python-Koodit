season = ("winter", "winter", "winter", "spring", "spring", "spring",
          "summer", "summer", "summer", "autumn", "autumn", "autumn")

no_of_months = int(input("Enter number of months (1- 12): " ))
print(f'the running season is {season[no_of_months - 1]}')



name_set = set()
while True:
    name = input("Enter a name:")
    if name == "":
        break

    if name in name_set:
        print("Already existed")
    else:
        print("New name")
    name_set.add(name)


for i in name_set:
    print(i)




def airport(fetch,store):
    for i in fetch:
        if i == store:
            return True
        return False

airports = {}
while True:
    print("\n")
    print("Do you want to add, search or exit for airports? (add, search, x)")
    command = input("Input: ")


    if command == "add":
        icoa = input("Enter ICOA code: ")
        if airport(airports, icoa):
            print("(Warning: The key is already in use!)")
            if input("Save new? (y/n): ") != "y":
                continue

        name = input("Enter the name of the airport: ")
        airports.update({icoa: name})
        print("Airport added")


    elif command == "search":
        icoa = input("Enter ICOA code: ")
        if airport(airports, icoa):
            print(f"Icoa code: {icoa} matches airport: {airports.get(icoa)}")
        else:
            print("No airport found")


    elif command == "x":
        print("Exiting the program...")
        break


    else:
        print("Wrong command")