# program to write into a file

cities_list = ['cairo', 'alex', 'mansoura', 'luxor']
with open('C:\\my_file\\write_cities.txt', 'a') as f:
    for i in range(len(cities_list)):
        if i == len(cities_list)-1: # here the last city
            f.write(cities_list[i])
        else:
            f.write(cities_list[i]+'\n')