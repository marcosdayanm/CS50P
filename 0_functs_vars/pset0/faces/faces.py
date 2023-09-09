
def convert(txt):
    return txt.replace(":)", "\U0001F642").replace(":(", "\U0001F641")


def main():
    hey = input("How is your mood: ")
    mood = convert(hey)
    print(mood)
    return 0;

main()
