
while True:
    f = input('Fraction: ')
    f = f.strip(' ')

    try:
        div = f.split('/')
        x, y = div[0], div[1]
        x = int(x)
        y = int(y)
    except ValueError:
        print('Incorrect input, insert a fraction in a x/y format, try again')
        continue
    except IndexError:
        print('Incorrect input, insert a fraction in a x/y format, try again')
        continue

    if x>y:
        print('Incorrect format, x should be equal or less to y, try again')
        continue

    try:
        fuel = round((x/y) * 100)
    except ZeroDivisionError:
        print('Incorrect input, "y" can\'t be zero, try again')
        continue

    if fuel <= 1:
        print('E')
    elif fuel >= 99:
        print('F')
    else:
        print(str(int(fuel)) + '%')

    break