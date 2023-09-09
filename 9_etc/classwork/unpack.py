'''
Ya hemos hecho ésto manualmente
Manera convencional de hacerlo:

first, _ = input('What\'s your name? ').split(' ')
print(f'Hello, {first}')
'''


def total(g=0,s=0,k=0):
    return (g*17 + s)* 29 + k

# coins = [100, 50, 25]

# Se puede unpackear un diccionario con **dictname solo que las keys se deben de llamar exactamente igual a los argumentos de las funciones
coins = {'g':100, 's':50, 'k':25}

# Ësta es la syntax de Python para unpackear algo, es decir, pasar los miembros individuales de una lista
print(total(**coins), 'Knuts')

# Ésta es la sintaxis para recibir un número variable de argumentos
# *args se refiere a los argumentos pasados como unna lista, y **kwargs se refiere a los argumentos pasados como un diccionario
# No se tienen que llamar de ésta manera, solo pesta es la convención para referirse a ésto
def f(*args, **kwargs):
    print('Positional:', args)
    print('Named:', kwargs)


f(100,s=50,k=25)
