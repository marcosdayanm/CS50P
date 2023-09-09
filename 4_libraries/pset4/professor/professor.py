import random

def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue
        if level < 1 or level > 3:
            continue
        return level


def generate_integer(level):
    if level == 1:
        num = random.randint(0,9)
    elif level == 2:
        num = random.randint(10,99)
    else:
        num = random.randint(100,999)
    return num


def operation(x, y):
    for i in range(3):
        try:
            op = int(input(f'{x} + {y} = '))
        except ValueError:
            print('EEE')
            continue
        else:
            result = x + y
            if op == result:
                return 0
            else:
                print('EEE')
    print(f'{x} + {y} = {result}')
    return 1


def main():
    score = 10
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        op = operation(x,y)
        if op == 1:
            score -= 1

    print(f'Score: {score}')



if __name__ == "__main__":
    main()