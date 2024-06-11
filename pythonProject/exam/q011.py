print('-- Solve password validation--')


def password(pass_value):
    count_lower, count_upper, count_digit, count_signs = 0,0,0,0
    if len(pass_value)>=8:
        for letter in pass_value:
            if letter.islower():
                count_lower = count_lower + 1
            elif letter.isupper():
                count_upper = count_upper + 1
            elif letter.isdigit():
                count_digit = count_digit + 1
            elif not letter.isalnum():
                count_signs = count_signs + 1
        if count_lower > 0 and count_upper > 0 and count_digit > 0 and count_signs > 0:
            print('password is valid')
        else:
            print('password not valid')

    else:
        print('not valid password')


str1 = 'sr@m@_f0rtu9e$._2023'
v_result = password(str1)
print(v_result)

