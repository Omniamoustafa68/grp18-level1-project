print('Remove all characters except letters and numbers')


def ini_string(statement):
    new_statement=''
    for letter in statement:
        if letter.isalnum():
            new_statement = new_statement + letter
    return new_statement


str1 = "123abcjw:, .@! eiw"
v_result = ini_string(str1)
print(v_result)