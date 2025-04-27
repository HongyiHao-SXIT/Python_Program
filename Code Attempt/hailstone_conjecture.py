def hailstone_conjecture(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

start_number = int(input("Please enter a number: "))
result = hailstone_conjecture(start_number)
print(f"The hailstone sequence starting from {start_number} is: {result}")