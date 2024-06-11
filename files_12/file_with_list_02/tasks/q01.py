new_lines_list =[]
total = 0
with open('C:\\my_file\\read2_data.txt','r') as f:
    lines_list = f.readlines()
    for line in lines_list:
        line = line.strip()
        new_lines_list.append(line)
        total = total + int(line)
        average = total/len(new_lines_list)
print(new_lines_list)
print('sum = ',total)
print('average = ',average)

