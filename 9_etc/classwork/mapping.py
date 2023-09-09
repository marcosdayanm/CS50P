def main():
    yell("This", "is", "CS50")


def yell(*words):
    '''
    Mapping:
    # Map aplica la misma función a una serie de elementos de un conjunto, o podemos pasarle múltiples elementos.
    uppercased = map(str.upper, words)
    '''
    # List comprehensions
    # Ésto hace que se aplique la función y se haga append a cada elemento de una lista a otra lista, es una forma Pythonic de hacer ésto
    upercased = [w.upper() for w in words]

    print(*uppercased)


if __name__ == "__main__":
    main()