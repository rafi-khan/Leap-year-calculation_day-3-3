print("Leap year calculator")
inserted_number = int(input("Insert a number to findout if it's leap year or not\n"))

if inserted_number % 4 == 0:

    if inserted_number % 100 == 0:

        if inserted_number % 400 == 0:
            print("Leap year")
            
        else:
            print("Not a leap")

    else:
        print("It's a leap year")

else:
    print("Not a leap year")