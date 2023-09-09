print('\nEnergy calculator according to Einstein\'s formula E=mc^2 \n')

c = 300000000 #m/s

m = float(input('Enter your mass: '))

E = m*c**2

E = "{:.0f}".format(E)

print(f'The energy calculated is: {E} J')
