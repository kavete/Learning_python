class Account:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def show_balance(self):
        print(f"Balance for { self.account_no } is Ksh { self.balance }")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account1 = Account("Brian", 127654, 560000)

account2 = Account("Etevak", 34562, 123000)


account1.deposit(5000)
account1.show_balance()
account1.withdraw(2000)
account1.show_balance()
