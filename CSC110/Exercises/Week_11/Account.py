class Account:
    InterestRate = 3/100

    def __init__(self, identification, balance, data_created):
        self.identification = identification
        self.balance = balance
        self.data_created = data_created

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def get_monthly_interest_rate(self):
        return self.InterestRate

    def get_monthly_interest(self):
        monthly_interest = self.balance * self.InterestRate
        return monthly_interest


a1 = Account('123', 500, '11112021')
print('Account ID:', a1.identification)
print('Account Balance:', a1.balance)
print("Month's IR:", a1.InterestRate)
print("Month's earned interest:", a1.get_monthly_interest())

a1.deposit(500)
print('New Balance:', a1.balance)

a1.withdraw(250)
print('New Balance:', a1.balance)



