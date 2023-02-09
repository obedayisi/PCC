number = input("Enter a number and I'll tell you whether it's a mulple of 10 or not: ")
number = int(number)

if 10 % number == 0:
    print(f"\n{number} is a multiple of 10")
else:
    print(f"\n{number} is not a multiple of 10")