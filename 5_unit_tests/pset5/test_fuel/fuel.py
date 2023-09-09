def convert(f):
    f = f.strip(' ')

    try:
        div = f.split('/')
        x, y = div[0], div[1]
        x = int(x)
        y = int(y)
    except ValueError:
        print('Incorrect input, insert a fraction in a x/y format, try again')
        return 404
    except IndexError:
        print('Incorrect input, insert a fraction in a x/y format, try again')
        return 404

    if x>y:
        print('Incorrect format, x should be equal or less to y, try again')
        return 404

    try:
        fuel = round((x/y) * 100)
    except ZeroDivisionError:
        print('Incorrect input, "y" can\'t be zero, try again')
        return 404
    else:
        return fuel


def gauge(fuel):
    if fuel <= 1:
        return 'E'
    elif fuel >= 99:
        return 'F'
    else:
        return str(int(fuel)) + '%'



def main():
    while True:
        f = input('Fraction: ')
        frac = convert(f)
        if frac == 404:
            continue
        break
    state = gauge(frac)
    print(state)



if __name__ == "__main__":
    main()