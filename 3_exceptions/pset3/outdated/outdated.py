
while True:
    months = {
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12"
    }

    date = input('Date: ').strip(' ')

    try:
        m, d, y = date.split('/')
        x = 1
    except ValueError:
        try:
            m, d, y = date.split(' ')
            x = 2
        except ValueError:
            continue


    if x == 1:
        try:
            im, id = int(m), int(d)
            if (im > 12) or (id > 31):
                continue

        except ValueError:
            continue
        else:
            if (im < 10) and (m[0] != '0'):
                m = '0' + m

            if (id < 10) and (d[0] != '0'):
                d = '0' + d


    elif x == 2:
        try:
            m = months[m]
            if d[-1] != ',':
                continue
            d = d.strip(',')
        except KeyError:
            continue
        else:
            try:
                id = int(d)
                if id > 31:
                    continue
            except ValueError:
                continue
            else:
                if (id < 10) and (d[0] != '0'):
                    d = '0' + d


    print(f'{y}-{m}-{d}')
    break
