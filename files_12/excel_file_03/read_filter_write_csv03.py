#program to read from excel and filter data based on cairo and write to another excel file
import csv
with open('C:\\my_file\\people1.csv', 'r') as f1, open('C:\\my_file\\people_filtered.csv', 'w', newline='') as f2:
    reader_list = csv.reader(f1)
    writer_pen = csv.writer(f2)
    writer_pen.writerow(['name', 'age', 'city'])
    for row in reader_list:
        if row[2] == 'cairo':
            writer_pen.writerow(row)