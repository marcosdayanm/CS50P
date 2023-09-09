q = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

q = q.strip(" ")

if q == '42':
    print('Yes')
else:
    q = q.lower().replace("-"," ")

    if q == 'forty two':
        print('Yes')
    else:
        print('No')

