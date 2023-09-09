import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

# Checar que los archivos dados como command line arguments sean csv
for i in range(1,3):
    if sys.argv[i][-4:] != '.csv':
        sys.exit('Not a CSV file')

fullname = [{'first':'first', 'last':'last'}]
house = [{'house':'house'}]
# Falta aladir el try y except
try:
    with open(sys.argv[1], 'r') as file1:
        reader = csv.DictReader(file1)
        for r in reader:
            l, f = r['name'].split(', ')
            fullname.append({'first':f, 'last':l})
            house.append({'house':r['house']})
except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')


with open(sys.argv[2], 'w') as file2:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file2, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(1,len(house)):
        writer.writerow({'first':fullname[x]["first"], 'last': fullname[x]["last"], 'house': house[x]["house"]})

'''
with open(sys.argv[2], 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        print(row['first'], row['last'], row['house'])
'''