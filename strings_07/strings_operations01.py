# show strings functions
print('---- Create and print string ----')
emp_name = 'yahia momtaz'
print(emp_name)
print(type(emp_name))


print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name) #yahia momtaz
print(upper_emp_name) #YAHIA MOMTAZ
print(lower_emp_name)#yahia momtaz
print(emp_name.title())  # Yahia Momtaz   # first alpha in words is upper


print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(upper_emp_name.isupper())#true
print(lower_emp_name.islower())#true
print(emp_name.isupper())#false
print(emp_name.isalpha())#false
emp_code = '101'
print(emp_code.isalpha()) #false
print(emp_code.isdigit()) #true
emp_code='101abs'
print(emp_code.isalnum()) #true     #print(not emp_code.isalnum()) = signs


print('-------------- endsWith() function -----------------')
file_name = 'egypt.PdF'
file_name = file_name.lower()   # to make the name and extension small [egypt.pdf]
if file_name.endswith('pdf'):
    print('it is a book')
elif file_name.endswith('mp3') or file_name.endswith('wav'):
    print('it is a song')
else:
    print('unknown type')


print('-------------- startswith() function ---------')
emp_mobile = '01047041564'
if emp_mobile.startswith('010'):
    print('it is vodafone')
elif emp_mobile.startswith('011'):
    print('it is etisalat')
else:
    print('unknown mobile')



print('------ in membership ---------- to find a word in a string---')
emp_cv = 'i am a programmer , i am interest in python java c++'

if 'python' in emp_cv and 'java' in emp_cv:
    print('it is the wanted emp')
else:
    print('it is not wanted')


print('-------------- count function -----------')

emp_cv = ' iam a programmer , i am interest in python java c++, i am professional in PYTHON'
emp_cv = emp_cv.lower()
print('python keyword occurs times :', emp_cv.count('python'))



print('---------- index(),  replace() functions |  slicing---------------')
emp_email = 'yahia.momtaz.aly@gmail.com'
print(emp_email.index('@'))    #(yahia.momtaz@gmail.com) @ = index 12
user_name = emp_email[0: emp_email.index('@')]
print('user name = ', user_name)
domain_name = emp_email[emp_email.index('@') + 1 :]
print('domain name = ', domain_name)

#change username , replace . with space
user_real_name= user_name.replace('.', ' ') #change all '.' with ' '
print(user_real_name)
user_new_name= user_name.replace('.' , ' ', 1) #change first '.' only
print(user_new_name)


print('--------------- Looping :  Loop over letters of string -----------------------')
print('----for each loop----')
for letter in emp_email:
    print(letter)

print('---for i index loop---')
for i in range(len(emp_email)):
    print(emp_email[i])

print('---split() function to split words of a string into a list of words---')
my_course = ' java python oracle linux network'
courses_list = my_course.split()  # (.) (,) ( )
print(courses_list)
for course in courses_list:
    print(course)


print('------ return the list back to string using join() function --------')
courses_list.reverse()
new_courses = ' '.join(courses_list)  # ',' '.' '  '
print(new_courses)




print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')

print('--strip---')
student_address = '           addr : cairo '
print(student_address)
new_student_address= student_address.strip()  #remove spaces
print(new_student_address)

print('--swapcase-- ')
#convert words from capital to small or small to capital
emp_name = 'mostafa'
print(emp_name.swapcase())
emp_name2= 'MOSTAFA'
print(emp_name2.swapcase())

print('---find---')
my_name= 'my name is omnia moustafa'
print(my_name.find('omnia')) # find omnia in my_name in index 11 # find ('search', start, end) first occurrence
print(my_name.find('eman'))   # if not find ( ) in my_name print -1

print('---rfind---') #reverse find
x = 'my name is omnia moustafa, i love python'
print(x.rfind('i'))     #start search from last i and calculate from first index last occurrence
print(x.rfind('i', 1, 20)) #from index 1 to index 20

student_name=' marwan '
print(student_name)
print(student_name.strip())

