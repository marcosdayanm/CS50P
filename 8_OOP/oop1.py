class Student:
    # this is the function called when we perform the inicialization of the attributes of a class, with the constructor, its name is __init__ because the authors of Python decided that
    # El parámetro "self", que podría tener cualquier otro nombre pero por convención se pone siempre self, tiene que se rel primer argumento del método, y sirve para que podamos tener acceso al objeto que se creó en ese mismo instante, porque sino no podríamos tener acceso a peste, es algo por convención en Python que funciona de ésta forma
    # Lo que si se tiene que hacer es definir nuestro propio init method para nombrar los atributos como nosotros quetramos, entre otras cosas
    def __init__(self, n, h):
        # De ésta manera, estamos instalando éstos atributos en nuestro objeto vacío creado por el método, y los estamos almacenando en el espacio de la memoria designado cuando se llama al constructor desde el mail program
        self.name = n
        self.house = h # éstab línea tambiéen va a llamar al setter, entonces podremos tener todo el error checking en un solo lugar


    def __str__(self):   # Método que Python ejecuta automáticamente al printear el objeto en sí
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        if not n:
            raise ValueError("Missing name")
        self._name = n


    # Getter: Función que da un atributo
    @property # syntax de getter
    def house(self):
        return self._house # ésto se pone de ésta manera para que Python no se confunda entre el atributo y la función, podría ser cualquier cosa pero por convención es un guión bajo

    # Setter: Función que determina un atributo
    @house.setter # syntax de setter
    def house(self, h):
        if h not in ['Gryffindor', 'Ravernclaw', 'Hufflepuff', 'Slytherin']:
            raise ValueError("Invalid house")
        self._house = h

"""
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Koala":
                return "🦥"
            case "Gorilla":
                return "🦍"
            case _:
                return "Not found yet"
"""



def main():
    student = get_student()
    #student.house = "Number Four, Privet Drive"  # acá, la instancia de Python va a seleccionar el método "Setter" porque identifica el signo de igual, que quiere settear, no obtener. Lo hace porque lo definimos de ésta forma con los métodos en la clase
    print(student)

    student


def get_student():
    name = input('Name: ')
    house = input('House: ')
    return Student(name, house)  # constructor call (instanciate a student object for me) using the student class as a template, so every student has the same structure


if __name__ == '__main__':
    main()







