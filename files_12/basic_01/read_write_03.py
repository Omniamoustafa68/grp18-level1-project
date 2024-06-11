#program to read from file and write to another file


with open('C:\\my_file\\read_data.txt', 'r') as f:
    content = f.read()
    print(content)

with open('C:\\my_file\\write_data2.txt', 'w') as f:
    f.write(content)