def value(g):
    gc = g[:5].lower()

    if gc == 'hello':
        return 0

    g1 = g[:1].lower()

    if g1 == 'h':
        return 20
    else:
        return 100

def main():
    greeting = input('Greeting: ')
    print(f'${value(greeting)}')

if __name__ == "__main__":
    main()