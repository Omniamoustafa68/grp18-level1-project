print('--program to find those numbers which are divisible by 7 an 5, between 1500,2700--')
numbers=[]
for item in range(1500, 2700):
    if item % 7 == 0 and item % 5 == 0:
        numbers.append(str(item))

result = ','.join(numbers)
print(result)

