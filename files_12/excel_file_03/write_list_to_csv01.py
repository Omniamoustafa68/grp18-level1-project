#program to write a list of lists to excel [csv] file

import csv
people_list = [
    ['Name', 'Age', 'City'],
    ['Adham', 25, 'Assuit'],
    ['Esam', 30, 'Cairo'],
    ['Shady', 28, 'Mansoura']
]
with open('C:\\my_file\\people.csv', 'w', newline='') as my_file:
    write_pen = csv.writer(my_file)
    for row in people_list:
        write_pen.writerow(row)