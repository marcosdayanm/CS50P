def convert(time):
    time = time.split(':')
    h = int(time[0])
    m = int(time[1])
    return h + m/60


def main():
    time = input('Insert the hour in a 24h forrmat only hours and minutes, (Ex. 13:45): ')
    tnum = convert(time)

    if tnum >= 7 and tnum <=8:
        print('breakfast time')
    elif tnum >= 12 and tnum <=13:
        print('lunch time')
    elif tnum >= 18 and tnum <=19:
        print('dinner time')


if __name__ == "__main__":
    main()