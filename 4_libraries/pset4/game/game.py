import random

def verify(text):
    while True:
        try:
            x = int(input(f'{text}'))
        except ValueError:
            continue
        if x > 0:
            return x

level = verify('Level: ')
randnum = random.randint(1,level)

while True:

    while True:
        number = verify('Guess: ')
        if number <= level:
            break

    if number < randnum:
        print('Too small!')
        continue
    elif number > randnum:
        print('Too large!')
        continue
    else:
        print('Just right!')
        break
