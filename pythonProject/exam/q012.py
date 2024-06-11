print('--program to reverse a string words--')


def reverse_statement(statement):
    words = statement.split()
    words.reverse()
    after_reverse = ' '.join(words)

    return after_reverse


str1 = 'i like this program very much'

v_resuilt = reverse_statement(str1)
print(v_resuilt)
