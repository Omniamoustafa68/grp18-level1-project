with open('C:\\my_file\\read3_data.txt', 'r') as f:
    input_passwords_list = f.readlines()
    print(input_passwords_list)
    cleaned_password_list = []
    for line in input_passwords_list:
        line = line.strip()
        cleaned_password_list.append(line)

    print(cleaned_password_list)
    valid_passwords_list = []
    for password in cleaned_password_list: # Loop over passwords list
        upper_count, lower_count, digits_count, signs_count = 0, 0, 0, 0
        for letter in password: # loop over 1 password letters
            if letter.isupper():
                upper_count=upper_count+1
            elif letter.islower():
                lower_count=lower_count+1
            elif letter.isdigit():
                digits_count=digits_count+1
            elif not letter.isalnum():
                signs_count=signs_count+1
        if upper_count>0 and lower_count>0 and digits_count>0 and signs_count>0:
            valid_passwords_list.append(password)

print(valid_passwords_list)

with open('C:\\my_file\\valid_password.txt', 'w') as f:
    for i in range(len(valid_passwords_list)):
        if i == len(valid_passwords_list) - 1:  # here the last password
            f.write(valid_passwords_list[i])
        else:
            f.write(valid_passwords_list[i] + '\n')


