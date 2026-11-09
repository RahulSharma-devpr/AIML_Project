class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):             
        return self.__balance

acc = Account(1000)
print(acc.balance)     