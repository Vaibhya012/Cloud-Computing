class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("Total Bal is ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was debited")
        print("Total Bal is ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(1000, 54321)
acc1.debit(100)
acc1.credit(7000)