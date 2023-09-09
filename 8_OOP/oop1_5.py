class Student:
    def __init__(self, n, h):
        self.name = n
        self.house = h

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Podemos llamar éste método sin instanciar ninún objeto todavía, sino como crearíamos a los estudiantes
    @classmethod
    def get_s(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name, house)

 

def main():
    student = Student.get_s()
    print(student)


if __name__ == '__main__':
    main()




