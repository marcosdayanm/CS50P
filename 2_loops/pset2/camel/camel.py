camel = input('\nInsert a camelCase phrase: ')

ind = 0

for l in camel:
    asc = ord(l)
    if asc <= 90:
        camel = camel[:ind] + '_' + chr(asc+32) + camel[ind+1:]
        ind += 2
        continue
    ind += 1

print('snake_case: ', camel)


# la función ord() sirve para outputtear el código ascii de un char
# la función chr() sirve para outputtear el char a partir de un codigo ascii