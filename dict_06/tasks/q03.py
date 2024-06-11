print('--example library--')
book_dict = {'pages':'277', 'name':'gone girl', 'year': 2007}
print(book_dict)

print('--adding elements to a dictionary--')
book_dict['author'] = 'well max'
print(book_dict)

print('--accessing elements inside a dictionary--')
print(book_dict['name'])

print('--changing elements inside a dictionary--')
book_dict['year'] = 2010
print(book_dict)

print('--using loop to print keys and value--')
for key, value in book_dict.items():
    print(key, value)

print('--removing items from a dictionary--')
book_dict.pop('name')
print(book_dict)