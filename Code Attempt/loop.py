magicians = ['Alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(digits)

min_digits = min(digits)
max_digits = max(digits)
sum_digits = sum(digits)
print("The min number in digits is " + str(min_digits))
print("The max number in digits is " + str(max_digits))
print("The total of the numbers in digits is " + str(sum_digits))

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

