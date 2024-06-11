print('--program to capitalize the first and last letters--')

str1 = 'python exercises practice solution'

str1 = str1.title()
words = str1.split()
print(words)
str2 = ''
for word in words:
    str2 = str2 + word[:-1] + word[-1].upper()+' '

str2 = str2[:-1]
print(str2)









