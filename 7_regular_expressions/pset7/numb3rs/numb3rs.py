import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r'^.{1,3}\..{1,3}\..{1,3}\..{1,3}$', ip):
        return False

    ipsp = ip.split('.')
    if len(ipsp) != 4:
        return False


    for i in range(4):
        try:
            ipi = int(ipsp[i])
        except ValueError:
            return False
        if ipi < 0 or ipi > 255:
            return False

    return True


if __name__ == "__main__":
    main()