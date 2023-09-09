import csv

name = input('What\'s your name? ')
home = input('Where\'s your home? ')

with open('addstud.csv','a') as file:
    writer = csv.DictWriter(file, fieldnames = ['name', 'home'])     # Función de csv que va a permitir añadir líneas a un file con un formato de diccionario, le tenemos que pasar los encabezados de las columnas en formato de lista con el orden en el que queremos que nos ordene los elementos
    writer.writerow({'home':home, 'name':name})  # De ésta manera se añaden líneas a un csv file, pasamos los argumentos como un diccionario con key y value para que los ponga en el orden de los encabezados
    # al usar writerow como un diccionario, podemos pasarle los argumentos desordenados pero como está con keys y values, va a escribir las columnas en el orden que especificamos en DictWriter


# Si escribimos una frase larga que tenga comas y la tratamos de appendear, el módulo nos pondrá las comillas en el csv utompaticamente

