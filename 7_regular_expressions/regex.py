import re

email = input('Insert your mail: ').strip()

# [^@] signifca que admita todos los carácteres excepto el arroba
# la "r" sirve para decirle a Pyhton que es un rawstring, que entienda que el backslash es una key, no un caracter que tiene que buscar
# a lo que hace referencia "\w" es a todos los carácteres alfanuméricos, es como si pusieramos en vez de eso [a-zA-Z0-9_]
# le estamos pasando una flag que hace que se ignoren las uppercase, y se transformen a lowercase
if re.search(r'^(\w+\.)?\w+@(\w+\.)?\w+\.(com|edu|org|net|mx|io)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')




