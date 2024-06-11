print('--count occurrences of a word in string--')

str = 'A computer science portal for portal'
words = str.split()
word_to_count= 'portal'
count_portal= 0
for word in words:
    if word_to_count in word:
        count_portal= count_portal+1

print('count occurrences of portal = ',count_portal)


#word == word_to_count