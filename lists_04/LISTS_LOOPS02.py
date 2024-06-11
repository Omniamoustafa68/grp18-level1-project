print('--- loop over elements of a list using for i index loop ---')
numbers_list = [14, 20, 5, 16, 10]
total = 0
for i in range( len(numbers_list) ):
    print(i, numbers_list[i] )
    total = total + numbers_list[i]
print('sum = ', total)
print( 'sum = ', sum(numbers_list) ) # built in function

print('--- loop over elements of a list using for each loop ---')
total=0 # reset total
for item in numbers_list:
    print(item) #numbers_list[i]
    total = total + item
print('sum = ', total)
print( 'sum = ', sum(numbers_list) ) # built in function