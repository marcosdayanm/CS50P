import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

namefile = sys.argv[1]

extension = namefile[-3:]
if extension != '.py':
    sys.exit('Not a Python file')

lines = []
try:
    with open(namefile,'r') as pyfile:
        for l in pyfile:
            if l.strip():
                lines.append(l.rstrip().strip())
                continue

except FileNotFoundError:
    sys.exit('File does not exist')

newlines = []
for i in range(len(lines)):
    if (lines[i][0] == '#'):
        continue
    else:
        newlines.append(i)
        #print(newlines)

print(len(newlines))