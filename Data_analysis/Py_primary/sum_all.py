def num_all(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    print(sum)

num = int(input("Please enter the number: "))
num_all(num)
