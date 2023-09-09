
def shorten(word):
    vocals = ['a', 'e', 'i', 'o', 'u']
    c = 0

    for i in word:
        if i.lower() in vocals:
            word = word[:c] + word [c+1:]
            c -= 1
        c += 1
    word = word.strip(' ')
    return word


def main():
    word = input('Input: ')
    shortword = shorten(word)
    print('Output:', shortword)


if __name__ == "__main__":
    main()