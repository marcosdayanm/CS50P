balance = 0


def deposit(n):
    global balance # Esta keyword balance se pone para decirle a python que esta variable es global, para que se pueda cambiar
    balance += n


def withdraw(n):
    global balance
    balance -= n


def main():
    print('Balance:', balance) # Se va a poder accesar a la variable global desde cualquier función, pero si quieres cambiar la variable, debe de ser local a la función
    deposit(100)
    withdraw(50)
    print('Balance:', balance)


if __name__ == '__main__':
    main()