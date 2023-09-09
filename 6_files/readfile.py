names = []

with open('names.txt') as file:
    for line in sorted(file):   # Se puede aplicar el método sorted() a la variable file
        names.append(line.rstrip())   # rstrip() para borrar el \n que se puso para que se salte la línea en el .txt

for n in names:
    print(f'hello, {n}')

