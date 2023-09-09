class Jar:
    def __init__(self, capacity=12, quantity=0):
        self.capacity = capacity
        self.quantity = quantity

    def __str__(self):
        return self.quantity*'🍪'

    def deposit(self, n):
        if self.quantity + n > self.capacity:
            raise ValueError('The cookies do not fit in the jar')
        self.quantity += n

    def withdraw(self, n):
        if self.quantity - n < 0:
            raise ValueError('You are trying to withdraw more cookies that the existant in the jar')
        self.quantity -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, x):
        if x < 0:
            raise ValueError('The capacity can not be negative')
        self._capacity = x

    @property
    def quantity(self):
        return self._quantity


    @quantity.setter
    def quantity(self, x):
        self._quantity = x




def main():
    jar = Jar()

    jar.deposit(6)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.quantity)
    print(jar)



if __name__ == '__main__':
    main()