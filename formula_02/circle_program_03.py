import math # call math module || to use pow() function

print('---- program to calculate area, perimeter of circle ----')
# input : pi | radius
# output : area | perimeter

radius = 7
pi = math.pi

perimeter = 2 * pi * radius

area = pi * math.pow(radius, 2)

print('perimeter = ', perimeter)
print('area = ', area)

print('perimeter = ' , round(perimeter, 2))
print('area = ', round(area, 2))