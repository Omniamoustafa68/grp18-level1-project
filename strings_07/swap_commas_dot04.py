print('---swap dots and commas---')
statement ='he is ahmed, ahmed lives in cairo, ahmed plays football.'
statement= statement.replace(',', '_')   #put a temp sign
statement= statement.replace('.',',')
statement=statement.replace('_', '.')
print(statement)