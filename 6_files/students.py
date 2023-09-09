import csv     # módulo para gestionar y trabajar con csv

students = []

with open('students.csv') as file:
    reader = csv.DictReader(file)   # función de csv que lee el archivo y cada linea la guarda como un diccionario de columnas (tienen que ser el mismo número de filas que las del encabezado) en donde la key va a ser el encabezado del file y el value, el elemento de su columna, iteradamente para cada fila
    for row in reader:  # a name y a home se le va a guardar a cada una, cada elemento de la lista que reader creó para leer el archivo csv
        students.append({'name':row["name"], 'home':row["home"]})


# Hacer una función que nos de el nombre, para que obtengamos todos los nombres de los diccionarios y podamos sortear en base a eso, se puede usar en la key, pero mejor usar una anonymous function (lambda)
def get_name(student):
    return student['name']

# we are passing to the sorted function as a parameter, a function to sort on the dictionary, to indicate it how to sort the dictionaries
# se va a llamar la función get_name en cada diccionario de la lista, la función sorted() va a llamar la función automáticamente
# la función lambda se declara en la key, y tiene edse formato, lambda es la keyword ya que la función no necesita un nombre
for s in sorted(students, key=lambda student: student['name'], reverse=False):
    print(f"{s['name']} belongs to {s['home']} ")




