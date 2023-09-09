class Vault:
    def __init__(self, g=0, s=0, k=0):
        self.galleons = g
        self.sickes = s
        self.knuts = k


    def __str__(self):
        return f'Galleons: {self.galleons} \nSickes: {self.sickes} \nKnuts: {self.knuts} \n'

    # Método que tenemos que declarar para que se puedan sumar elementos de dos clases diferentes
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickes = self.sickes + other.sickes
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickes, knuts)



potter = Vault(100,50,25)
print(potter)


weasley = Vault(25, 50, 100)
print(weasley)


# Cuando python ve esto, usa la función declarada en la clase __add__
total = potter + weasley
print(total)


