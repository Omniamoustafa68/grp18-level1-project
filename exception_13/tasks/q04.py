def extract_element(list, index):
     try:
         return list[index]
     except IndexError:
         return 'index out of range'


v_result = extract_element([10, 20, 30],  5)
print(v_result)
