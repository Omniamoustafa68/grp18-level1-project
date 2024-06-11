#program to write into text file
#1- open for write
#2- operation(write)
#3- close file

print('---first way---')
my_file = open('C:\\my_file\\write_data.txt', 'w')
my_file.write('i like programming\n')
my_file.write('i like football\n\n')
my_file.write('python is a programming language')
my_file.close()

print('---second way---')
with open('C:\\my_file\\write_data.txt', 'a') as f:    #a for append like in list lesson
    f.write('\n+++++++++++++++++\n')
    f.write('python is the basic programming for ai\n')
    f.write('you should learn django for python backend development')


