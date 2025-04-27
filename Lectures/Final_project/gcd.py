def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
num1, num2 = int(num1), int(num2)
result = gcd(num1, num2)
print(f"The greatest common divisor of {num1} and {num2} is: {result}")