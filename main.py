print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))
if height >= 48:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age < 18:
        print("Please pay $7.")
    elif age > 64:
        print("Please pay $6.")
    else:
        print("Please pay $12.")
else:
    print("You are not tall enough to ride.")
