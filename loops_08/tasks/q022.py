print('--program to find those numbers which are divisible by 7 an 5, between 1500,2700--')

result= []

for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)

print(result)


