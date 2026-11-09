class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self.history = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self._balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
            return
        self._balance -= amount
        self.history.append(("withdraw", amount))

    def __str__(self):
        return f"{self.owner}: Rs {self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.04):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self._balance * self.rate)

    def withdraw(self, amount):            # override: keep a minimum balance
        if self._balance - amount < 500:
            print("Minimum balance of 500 required")
            return
        super().withdraw(amount)


acc = BankAccount("Asha", 2000)
acc.deposit(500)
acc.withdraw(300)
print(acc)

sav = SavingsAccount("Ravi", 1000)
sav.add_interest()
sav.withdraw(900)      # blocked by the minimum balance rule
print(sav, sav.history)