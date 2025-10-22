class Account:
    def __init__(self, balance, name):
        if balance < 0:
            raise ValueError("The opening balance cannot be negative.")
        else:
            self.balance = balance
            self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("You cannot deposit a negative amount.")
        else:
            self.balance += amount

    def take(self, amount):
        if amount > self.balance:
            raise ValueError("No funds in your account.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Name: {self.name}; balance: {self.balance}"

account = None
try:
    account = Account(-20, "Account 1")
    print(account)
except ValueError as v:
    print(v)

try:
    account = Account(200, "Account 2")
    print(account)
except ValueError as v:
    print(v)

try:
    account.deposit(-20)
    print(account)
except ValueError as v:
    print(v)

try:
    account.deposit(20)
    print(account)
except ValueError as v:
    print(v)

try:
    account.take(1350)
    print(account)
except ValueError as v:
    print(v)

try:
    account.take(135)
    print(account)
except ValueError as v:
    print(v)
