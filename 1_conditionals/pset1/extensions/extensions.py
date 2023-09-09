def main():
    f = input('Filename: ')

    if '.' not in f:
        print(f'application/octet-stream')
        return 0

    split = f.split('.')
    ext = split[-1].lower().strip(" ")

    if ext == 'gif' or ext == 'jpeg' or ext == 'png':
        print(f'image/{ext}')
    elif ext == 'jpg':
        print(f'image/jpeg')
    elif ext == 'pdf' or ext == 'zip':
        print(f'application/{ext}')
    elif ext == 'txt':
        print('text/plain')
    else:
        print(f'application/octet-stream')
    return 0


main()