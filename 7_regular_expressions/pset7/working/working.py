import re
import sys

def main():
    print(convert(input("Hours: ").strip()))


def situations(h, t):
    if t == 'PM':
        if h != '12':
            h = str(int(h) + 12)
    elif h == '12':
        h = '0'

    if int(h) < 10:
        h = '0' + h

    return h, t


def convert(s):
    x = re.search(r'^([0-9]{1,2})\:?([0-9]{2})? (AM|PM) to ([0-9]{1,2})\:?([0-9]{2})? (AM|PM)$', s)

    if x == None:
        raise ValueError("Invalid input string")
    elif x.group(2) == None and x.group(5) == None:
        fh, ft, sh, st = x.group(1), x.group(3), x.group(4), x.group(6)
        k = 1
    elif x.group(2) != None and x.group(5) != None:
        fh, fm, ft, sh, sm, st = x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)
        k = 2
        if int(fm) > 59 or int(sm) > 59:
            raise ValueError("Invalid input string")
    else:
        raise ValueError("Invalid input string")


    fh, ft = situations(fh, ft)
    sh, st = situations(sh, st)


    if k == 1:
        return (fh + ':00' + ' to ' + sh + ':00')
    else:
        return (fh + ':' + fm + ' to ' + sh + ':' + sm)


if __name__ == "__main__":
    main()
