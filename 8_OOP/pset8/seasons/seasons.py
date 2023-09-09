from datetime import date
import sys
import re
import inflect


def vali_date(today, fecha):
    if not re.search(r'^[0-9]{4}-{1}[0-9]{2}-{1}[0-9]{2}$', fecha):
        sys.exit('Invalid date')

    try:
        dateF = date.fromisoformat(fecha)
    except ValueError:
        sys.exit('Invalid date')


    if today < dateF:
        sys.exit('Invalid date')

    return today, dateF


def calc_mins(today, dateF):
    tiempo = today - dateF
    dias = int(str(tiempo).split(' ')[0])
    mins = dias*24*60
    return mins


def num_text(min):
    p = inflect.engine()
    txt = p.number_to_words(min).capitalize()

    if matches := re.search(r'^(.+)( and)(.+)$', txt):
        txt = matches.group(1) + matches.group(3)
        if matches := re.search(r'^(.+)( and)(.+)$', txt):
            txt = matches.group(1) + matches.group(3)

    return txt + ' minutes'




def main():
    now = date.today()
    fecha = input('Insert your birth date in the format YYYY-MM-DD: ')
    today, dateF = vali_date(now, fecha)
    minutos = calc_mins(today, dateF)
    print(num_text(minutos))







if __name__ == "__main__":
    main()