import re

name = input('What\'s your name? ')

# Éste operador nuevo (:=), permite asignarle el return de una funcióna. una variable, y al mismo tiempo aplicarle un if statement
if matches := re.search(r'^(.+), ?(.+)$', name):
    # Ésta es una manera simplificada de hacer el mismo proceso pero sinn la necesidad de guardarlo en una variable previamente
    # Acorde a la documentación de pesta función, el primer elemento va a empezar con "1"
    name = matches.group(2) + " " + matches.group(1)
print(f'hello, {name}')



