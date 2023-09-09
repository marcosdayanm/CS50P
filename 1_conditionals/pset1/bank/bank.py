def main():

    g = input('Greeting: ')
    gc = g[:5].lower()

    if gc == 'hello':
        print('$0')
        return 0

    g1 = g[:1].lower()

    if g1 == 'h':
        print('$20')
        return 0
    else:
        print('$100')
        return 0

main()
