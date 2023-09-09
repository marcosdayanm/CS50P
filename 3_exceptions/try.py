def get_int(text):
    while True:
        try:
            return  int(input(f'{text}'))  # más eficiente hacerlo de esta manera, sin declarar ninguna variable
        except ValueError:    # Es importante especificar qué tipo de error se puede tener, ya que si se espera todo tipo de error, Python puede cachar otro error del codigo y no lo detectaríamos nunca
            print('The number you inserted isn\'t an integer, try again \n')
            #pass #esta keyword es para ignorar y solo pasar este error, sino queremos imprimir nada la podemos usar


def main():
    x = get_int('Num: ')
    print(f'Number is:', x)


if __name__ == '__main__':
    main()
