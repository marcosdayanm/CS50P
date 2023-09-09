# Lists Comprehensions

students = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Hermione', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Gryffindor'},
    {'name': 'Draco', 'house': 'Slytherin'},
]

'''
# Podemos usar el list comprehension también de ésta manera
gryffindors = [
    s['name'] for s in students if s['house'] == 'Gryffindor'
]

for g in sorted(gryffindors):
    print(g)
'''


def is_g(s):
    return s['house'] == 'Gryffindor'

gryffindors = filter(is_g, students)

for g in gryffindors:
    print(g['name'])


