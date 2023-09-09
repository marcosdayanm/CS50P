import argparse

'''
import sys

if len(sys.argv) == 1:
    print('meow')

elif len(sys.argv) == 3 and sys.argv[1] == '-n':
    n = int(sys.argv[2])
    for _ in range(n):
        print('meow')

else:
    print('usage: meows.py')
'''

# Ésta librería funciona primero llamando el constructor de cierta clase, el parámetro "description" es opcional y solo sirve para pasarle info al usuario
parser = argparse.ArgumentParser(description='Meow like a cat')
# Ésto sirve para buscar cierto command line argument y su dato posterior, hay un valor default por si no se cumple la condición
parser.add_argument('-n', default=1, help='number of times to meow', type=int)
# acá accedemos a éste método que me imagino que tiene que ver con los argumentos y su número
args = parser.parse_args()


for _ in range(args.n):
    print('meow')

