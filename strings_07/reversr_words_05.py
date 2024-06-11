print('---program to reverse words of string---')

statement= 'i like this program very much'
#convert string to a list using split
words_list=statement.split()
words_list.reverse()
print(words_list)


#convert the list back to string
statement= ' '.join(words_list)
print(statement)