#Read csv, validate password with valid complexity and write them to another csv file
import csv
with open('C:\\my_file2\\password_valid.csv', 'r') as file:
    reader = csv.reader(file)
    reader_list= []
    next(reader)
    for row in reader:
        reader_list.append(row)
    print(reader_list)
    valid_passwords =[]
    for passwords in reader_list:
        upper_count, lower_count, digits_count, signs_count = 0, 0, 0, 0
        for letter in passwords[1]:
            if letter.isupper():
                upper_count = upper_count+1
            elif letter.islower():
                lower_count = lower_count +1
            elif letter.isdigit():
                digits_count = digits_count+1
            elif not letter.isalnum():
                signs_count = signs_count+1
        if upper_count>0 and lower_count>0 and digits_count>0 and signs_count>0:
            valid_passwords.append(passwords)
print(valid_passwords)

with open('C:\\my_file2\\valid_password.csv', 'w', newline='') as files:
    writer_pen = csv.writer(files)
    writer_pen.writerows(valid_passwords)
