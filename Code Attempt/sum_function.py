n = int(input("Enter n: "))
a = int(input("Enter a (0~9): "))

time = 0

total = 0
term = 0
for time in range(n):
    term = term * 10 + a
    total += term
    time += 1
print("Result:", total)
