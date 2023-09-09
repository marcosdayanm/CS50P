def main():
    op = input('Insert your operation in a number space operation space number format, (Ex. 1 + 1): ')
    opr = op.split(" ")

    x, y, z = float(opr[0]), opr[1], float(opr[2])

    if y == '+':
        print(x+z)
    elif y == '-':
        print(x-z)
    elif y == '*':
        print(x*z)
    elif y == '/':
        if z == 0:
            print('Invalid operation, try again')
            return 0
        print(x/z)
    return 0

main()