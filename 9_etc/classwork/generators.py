
def main():
    n = int(input('What\'s n? '))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(1, n+1):
        yield "🐑"*i # Ésta keyword significa regresar un valor cada vez, el loop seguriá trabajando

if __name__ == '__main__':
    main()