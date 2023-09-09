import emoji
import sys

t = input('Input: ')
t = t.strip(' ')

if ':' not in t:
    sys.exit()

code = t.split(':')
emo = ':' + code[1] + ':'
message = code[0] + emo

print(emoji.emojize(message))