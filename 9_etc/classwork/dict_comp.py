# Dictionary Comprehensions

students = ['Hermione', 'Harry', 'Ron']

# Enumerate
for i, student in enumerate(students):
    print(i+1, students)

'''
Manera convencional:
gryffs = []
for s in students:
    gryffs.append({'name':s, 'house':'Gryffindor'})
'''

# Acá se hace también con una lista, pero utilizando la herramienta de un dicionario
#gryffs = [{'name':s, 'house':'Gryffindor'} for s in students]

# Acá se hace directamente con un diccionario
gryffs = {s: 'Gryffindor' for s in students}

print(gryffs)
