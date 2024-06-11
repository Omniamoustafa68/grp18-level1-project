print('--- program to check for person age ----')
person_age = input('please enter your age : ')
person_age = int(person_age)        # casting : convert from data type to int data type
print(person_age)
print(type(person_age))

person_age = 18

"""
if person_age > 16:
   print('you are a man')
elif person_age >= 11 and person_age <=16:
    print('you are a boy')
elif person_age >= 0: 
     print(' you are a child')
 else : 
    print ('invaild age')           
"""
if person_age > 16:
    print('you are a man')
elif person_age >= 11:
    print(' you are a boy')
elif person_age >=0:
    print('you are a child')
else:
    print('invaild age')