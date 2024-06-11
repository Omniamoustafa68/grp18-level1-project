#creat a function to print numbers from 1 > 10  1 usage

def print_numbers(max_num):
    total = 0
    for i in range(1, max_num + 1):
        print(i, end=' ')
        total = total + i  # to calculate summation of numbers from 1 to max_num
    return  total
#main program
#call (invoke) the function
print('--program to show user defined functions with parameters and return sum of numbers---')
#v_result = print_numbers(10)
v_result = print_numbers(max_num=10)
print()
print( 'the result from first call=',v_result)
#v_result= print_numbers(20)
v_result = print_numbers(max_num=20)
print()
print( 'the result from second call=',v_result)
#v_result = print_numbers(30)
v_result = print_numbers(max_num=30)
print()
print('the result from third call=',v_result)