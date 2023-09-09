from calculator import square

def test_square():

    for i in range(-5,6,1):
        try:
            assert square(i) == i**2
        except AssertionError:
            print(f'{i} squared was not {i**2}')


def main():
    test_square()


if __name__ == '__main__':
    main()