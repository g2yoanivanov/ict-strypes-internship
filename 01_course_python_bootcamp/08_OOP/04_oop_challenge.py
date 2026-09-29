# OOP Challenge Task

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance = self.balance + sum

    def withdraw(self, sum):
        if sum > self.balance:
            print('Funds Unavailable')

        else:
            self.balance = self.balance - sum

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'


acc1 = BankAccount('Yoan', 500)
print(acc1)

acc1.deposit(670)
print(acc1)

acc1.withdraw(2000)
acc1.withdraw(450)
print(acc1)