# function to find a number in list : return its index oe -1 if not found



def find_number(my_list, value):
    if value in my_list:
       return my_list.index(value)
    else:
        return -1


list1 = [12, 15, 6, 10 , 9 ,20]
#v_result= find_number(list1, 10)
v_result = find_number(my_list=list1, value=10)
print(v_result)
