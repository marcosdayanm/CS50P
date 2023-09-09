import re


def main():
    print(count(input("Text: ")))


def count(s):
    lst = re.findall(r'(\bum\b)' , s, re.IGNORECASE)
    print(lst)
    return len(lst)


if __name__ == "__main__":
    main()