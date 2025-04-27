import math

radiusString = input("Enter the radius of your circle: ")

radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print(f"The circumference is: {circumference}, and the area is: {area}")
