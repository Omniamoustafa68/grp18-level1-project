#Read a CSV file and calculate the average value from a specific column
import csv
total = 0
average_age = []
with open('C:\\my_file2\\people.csv', 'r') as file:
    reader_list = csv.reader(file)
    next(reader_list)
    for row in reader_list:
        average_age.append(row[1])
        total = total + int(row[1])
        average = total / len(average_age)
print('Average from column 1 = ',average)


print(average_age)
