from pyfiglet import Figlet
import random
import sys

getf = Figlet().getFonts()

if len(sys.argv) == 3:
    comm = sys.argv[1]
    fo = sys.argv[2]
    if comm == '-f' or comm == '--font':
        if fo in getf:
            f = fo
        else:
            sys.exit('\nError, font not found, try again \n')
    else:
            sys.exit('\nError, in first command-line argument, try again \n')

elif len(sys.argv) == 1:
    f = random.choice(getf)
else:
    sys.exit('\nError, there should be zero or two command line arguments, try again \n')


font = Figlet(font=f)
text = input('Input: ')

print(font.renderText(text))
