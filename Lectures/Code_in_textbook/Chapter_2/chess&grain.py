n = 64
total_sum = 0
total_weight = 0

grain_weight = 50


def num_of_grains(n):

    angle = 4

    grains_in_angle = 2 ** (n - 1)

    total_num = angle * grains_in_angle
    return total_num


while n != 0:
    total_sum += num_of_grains(n)
    n -= 1

total_weight = (total_sum * grain_weight) / 1000000

print("The number of grains that the king should pay is", total_sum)
print("The weight of all of the grains is(kg): ", total_weight)