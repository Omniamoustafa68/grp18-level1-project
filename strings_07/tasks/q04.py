print('--write a program to remove dublicateed words--')
original_string= 'hello world world python is great great python'
string_list=original_string.split()
unique_list=[]
for item in string_list:
    if item not in unique_list:
        unique_list.append(item)

new_string=' '.join(unique_list)
print(new_string)
