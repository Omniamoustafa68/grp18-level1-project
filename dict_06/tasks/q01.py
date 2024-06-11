print('--converting a list of tuples to a dictionary--')

colors_list = [('red', 223), ('blue', 201), ('green', 201)]
color_dict = {}

for i in range(len(colors_list)):
    color_dict[colors_list[i][0]] = colors_list[i][1]
print(color_dict)