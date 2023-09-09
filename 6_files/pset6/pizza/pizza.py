import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

namefile = sys.argv[1]
extension = namefile[-4:]
if extension != '.csv':
    sys.exit('Not a CSV file')

lines = []
try:
    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            elem = []
            for e in row:
                elem.append(e)
            lines.append(elem)

except FileNotFoundError:
    sys.exit('File does not exist')

table, headers = lines[1:], lines[:1]
headers = headers[0]

# Format: table, headers, table format
print(tabulate(table, headers, tablefmt="grid"))