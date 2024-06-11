print('--make uppercase half string--')

str1= 'ArabRepublicOfEgypt'
half_string= len(str1)//2
upper_half = str1[0:half_string ].upper()
str2= upper_half + str1[half_string:]
print(str2)