
def IntegerNumber():
    arr = []
    while True:
        try:
            number = int(input("Please enter an integer: "))
            if number > 0:
                arr.append(number)
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            break
    return arr


print(IntegerNumber())