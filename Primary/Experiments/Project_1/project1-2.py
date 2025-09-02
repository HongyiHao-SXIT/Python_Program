def calculate_square(num):
    return num ** 2


num = float(input("Please enter a number: "))
square = calculate_square(num)
print(f"The square of {num} is: {square}")