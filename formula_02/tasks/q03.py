import math

print('-- program to calculate volume and surface area of sphere --')

# input = pi | radius
# output = volume | surface area

radius = 2
pi = math.pi
v = 4 / 3 * pi * math.pow(radius, 3)
a = 4 * pi * math.pow(radius, 2)

print('v = ', v)
print('a = ', a)