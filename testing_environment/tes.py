class CashRegister:
    def __init__(self): # Error 1 no init
        self._itemCount = 0
        self._totalPrice = 0.0

    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
    
    def getTotal(self):
        return self._totalPrice

cash = CashRegister()

cash.addItem(10.50)
cash.addItem(5.25)

total = cash.getTotal()
print(f'Total: {total}')

cash.clear()

total_after = cash.getTotal()
print(f'Total after: {total_after}')