def number_check(num):
    if 2 <= num <= 20 and num % 3 == 0:
        return True
    return False


while True:
    try:
        number = float(input("Please enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if number_check(number):
    print("This number is correct")
else:
    print("This number does not meet the criteria.")