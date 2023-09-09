import random

coin = random.choice(['Heads', 'Tails'])   # This function works like this, with an input and randomizes the output between the passed ones
print('Heads or tails:',coin)

integer = random.randint(1,10)   # This function will give me a random integer between these both parameters
print('Random integer:',integer)

cards = ['jack', 'queen', 'king']
print('Old order: ',end='')
for i in cards:
    print(i, end=' ')

random.shuffle(cards)   # Ésta función revuelve elementos de una lista y lo guarda en la misma variable en la que estaba
print('\nNew order: ',end='')
for i in cards:
    print(i, end=' ')