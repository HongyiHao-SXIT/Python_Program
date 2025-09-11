import math

r = float(input("Please enter the radius of the sphere: "))
area = 4 * math.pi * r * r
vol = 4 * math.pi * r ** 3 / 3
print("The sphere with radius %.2f has a surface area of %.2f and a volume of %.2f" % (r, area, vol))