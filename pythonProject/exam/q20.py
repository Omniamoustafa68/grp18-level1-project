str1 = 'i am excellent in python and python'
words_list= str1.split()
word_to_count = 'python'
count_word= 0
for word in words_list:
    if word_to_count == word:
        count_word = count_word + 1

print('Count occurrences of a word in string = ',count_word)