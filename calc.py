while (True):
    adding = 0
    subtracting = 0
    multiplying = 0
    dividing = 0
    num_1 = int(input("First number: "))
    num_2 = int(input("Second number: "))
    selection = input("Select calculation type (1. Adding, 2. Subtracting, 3. Multiplying, 4. Dividing): ")
    if selection == "1":
        adding = 1
        num1 = num_1 + num_2
        print(num1)
    elif selection == "2":
        subtracting = 1
        num1 = num_1 - num_2
        print(num1)
    elif selection == "3":
        multiplying = 1
        num1 = num_1 * num_2
        print(num1)
    elif selection == "4":
        dividing = 1
        num1 = num_1 / num_2
        print(num1)
    input('press enter to continue')

