'''
# Procedural Programming:
MEOWS = 3 # Ésta es la convención que se usa para declarar variables que no deben de swer cambiadas

for _ in range(MEOWS):
    print('meow')
'''

'''
# OOP Programming:
class Cat:
    MEOWS = 3 # Éstas variables afuera de todo son variables de la clase, es decir, que todos los objetos van a tener las mismas variables

    def meow(self):
        for _ in range(Cat.MEOWS):
            print('meow')

cat = Cat()
cat.meow()
'''


# Type hints
# Así se especifica que la variable debe de ser int, pero aún así Python no lo va a parar hasta que se tope con el error
def meow(n: int) -> None: # Así con esa notación se dice que el return value por default debería de ser None
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    """
    for _ in range(n):
        print('meow')

# Así tambien se instancia una type hint al declarar una variable
number: int = int(input('Number: '))
meow(number)
