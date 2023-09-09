from validator_collection import validators


def main():
    print(validate_mail(input('What\'s your email address? ')))


def validate_mail(e):
    try:
        validators.email(e)
    except ValueError:
        return 'Invalid'
    return 'Valid'


if __name__ == "__main__":
    main()