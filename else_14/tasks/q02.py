string = 'egypt'
specific_character = 'c'
for item in string:
    if item == specific_character:
        print('character is found in string')
        break
else:
    print('character is not found')
