import random

class Hat:

    # Class variables, only one copy for all the objects
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    @classmethod
    def sort(cls, name): # se usa la keyword "cls" por convención para hacer referencia no al objeto, sino a la clase ya que en esta clase no habrán objetos
        print(f"{name} is in {random.choice(cls.houses)}")

# Acá la clase funciona como si fuera un solo objeto
Hat.sort("Harry")


