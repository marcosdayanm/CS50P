class Wizard:
    def __init__(self, n):
        if not n:
            raise ValueError('Missing name')
        self.name = n
    ...



# De ésta forma, con el paréntesis se dice que esa clase hereda a la clase en paréntesis
class Student(Wizard):
    def __init__(self, n, h):
        super().__init__(n) # el super() hacer referencia a la clase padre, estamos llamando a su __init__ para inicializar el nombre
        self.house = h

    ...


class Professor(Wizard):
    def __init__(self, n, s):
        super().__init__(n)
        self.subject = s

    ...


wizard = Wizard('Albus')
student = Student('Harry', 'Gryffindor')
professor = Professor('Snape', 'Defence')

