# program to Read data from a CSV file and generate a bar chart
import csv
import matplotlib.pyplot as plt
with open('C:\\my_file2\\people.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # ignore the header
    x = []
    y = []
    for row in reader:
        x.append(row[0])
        y.append(float(row[1]))
    plt.bar(x, y)
    plt.xlabel('names')
    plt.ylabel('ages')
    plt.title('Bar Chart from CSV Data')
    plt.xticks(rotation=45) #rotate x-axis labels for readability
    plt.show()