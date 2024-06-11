# function to return true if it is even number or false if it is ood number

def check_number(value):
    if value % 2 == 0:
        return True
    else:
        return False


#main program
#v_result= check_number(7)
v_result = check_number(value=7)
if v_result:          # if v_result == true
    print('it is even')
else:
    print('it is ood')
