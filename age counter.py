try:
    age = input("Enter age: ")

    if age.isdigit():
        age = int(age)

        if age % 2 == 0:
            print("Age is even")
        else:
            print("Age is odd")
    else:
        raise ValueError

except ValueError:
    print("Invalid input. Please enter a whole number only")
    