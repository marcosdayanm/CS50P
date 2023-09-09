def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    lens = len(s)

    if lens < 2 or lens > 6:   # longitud
        return False

    elif ord(s[-1]) > 64 and ord(s[-1]) < 91:  # que no termine con numero
        return False

    elif s[2] == '0':  # no 0 el primer número
        return False



    for i in range(lens):
        ascnum = ord(s[i])
        haynum = (ascnum < 65 or ascnum > 90)
        solonum = (ascnum > 47 and ascnum < 58)

        if i<2:   # que empiece con 2 letras
            if haynum:
                return False
        elif i>2:
            if not solonum:
                return False


    return True

if __name__ == "__main__":
    main()