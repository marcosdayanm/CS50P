import sys     # Library that has methods related to the system

print('The name of the file is:',sys.argv[0]) # .argv es una función que va a regresar una lista de todos los comandos que se escribieron al ejecutar el codigo, el [0] es el nombre del archivo
'''
try:
    print('Hello,',sys.argv[1])
except IndexError:
    print('Error, you need to enter minimum one command-line argument, try again')
'''

if len(sys.argv) < 2:
    print('Too few arguments')

for arg in sys.argv[1:]:   # Con el paréntesis estamos agarrando un slice de la lista
    print('Hello,', arg)


# sys.exit() will exit the program, it allows to enter an output to the user in between the parenthesis of the function