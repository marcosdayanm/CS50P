lista = dict()

while True:

    try:
        item = input().upper()
    except EOFError:
        break

    if item in lista:
        lista[item] += 1
    else:
        lista[item] = 1

print()   # format

for k in lista:
    print(f'{lista[k]} {k}')
