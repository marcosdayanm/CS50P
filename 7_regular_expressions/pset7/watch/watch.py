import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    x = re.search(r'^.*"https?://(?:www\.)?youtube\.com/embed(/.+)(?:"(?:\st|><).+>)$', s)

    try:
        link ='https://youtu.be' + x.group(1)
    except AttributeError:
        return None

    return link





if __name__ == "__main__":
    main()