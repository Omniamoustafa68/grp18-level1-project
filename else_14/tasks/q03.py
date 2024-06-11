correct_password = '12345678'
attempts = 0
while attempts < 3:
    password = input('enter the password:')
    if password == correct_password:
        print('password correct')
        break
    else:
        attempts = attempts + 1

else:
    print('you have pass the maximum number of attempts ')