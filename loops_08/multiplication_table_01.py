print('--program to print ')

for i in range(1, 11):   # rows
    for j in range(1, 11): # colums
        if i * j < 10:
            print(i * j, end='  ')
        else:
            print(i * j, end=' ')
    print()  # enter (new line)