print('\n\nWelcome to the Coke Vending Machine. \nIt costs 50 cents, and we only accept 25, 10 and 5 cents coins')

amount = 0

while True:
    coin = int(input('Insert coins to buy the coke: '))
    if coin not in [5, 10, 25]:
        print('\nInvalid coin, try again...\n')
        continue
    amount += coin
    if amount >= 50:
        print('Change Owed:', amount - 50)
        break

    print('Amount Due:', 50 - amount)