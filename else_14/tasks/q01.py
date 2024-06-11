numbers = [1, 3, 5, 7, 9, 11]
for num in numbers:
    if num %2 ==0:
        print('the first even numbers ', num)
        break
else:
    print('no even numbers in the list')