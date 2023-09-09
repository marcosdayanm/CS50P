students = [
    {'name': 'Hermione', 'house': 'Gryffindor'},
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Gryffindor'},
    {'name': 'Draco', 'house': 'Slytherin'},
    {'name': 'Padma', 'house': 'Ravenclaw'},
]


houses = set()
for s in students:
    houses.add(s['house']) # En Python, el append de los sets es add

for house in sorted(houses):
    print(house)
