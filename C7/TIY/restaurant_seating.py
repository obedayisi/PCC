message = "Hello, welcome to Rahama Reastaurant"
message += "\nHow many people do you have in your dinner group? "

askGuest = input(message)
askGuest = int(askGuest)

if askGuest > 8:
    print("\nSorry, you'd have to wait for a table")
else:
    print("\nYour table is ready")