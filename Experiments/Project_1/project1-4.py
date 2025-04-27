import math
r = float(input("Please enter the radius: "))
sarea = 4 * math.pi * r * r
volume = 4 / 3 * math.pi * r ** 3
print(f"The surface area of the sphere: {sarea:.2f}")
print(f"The volume of the sphere: {volume:.2f}")