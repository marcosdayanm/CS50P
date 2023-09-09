word = input('Input: ')

vocals = ['a', 'e', 'i', 'o', 'u']
c = 0

for i in word:
    if i.lower() in vocals:
        word = word[:c] + word [c+1:]
        c -= 1
    c += 1

print('Output:', word)