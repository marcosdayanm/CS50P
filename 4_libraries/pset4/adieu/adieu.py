import sys

names = []

while True:
    try:
        name = input('Name: ')
    except EOFError:
        print('\n')
        break

    names.append(name)


lennames = len(names)
if lennames == 0:
    sys.exit()

print('Adieu, adieu, to ', end='')

for i in range(lennames):
    print(names[i], end='')

    if i < lennames - 2:
        print(', ', end='')
    elif i == lennames - 1:
        print('\n')
    else:
        print(', and ', end='')



