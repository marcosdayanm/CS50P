class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    juan = Account()
    print('Balance:', juan.balance)
    juan.deposit(100)
    print('Balance:', juan.balance)
    juan.withdraw(50)
    print('Balance:', juan.balance)


if __name__ == '__main__':
    main()