from customer_impl import CustomerImpl

class Account(CustomerImpl):

    def __init__(self, name, id, amount, diposit, withdraw):
        super(Account, self).__init__(name=name, id=id)
        self.amount = amount
        self.diposit = diposit
        self.withdraw = withdraw
        self.accountblnc=0.0

    def get_payment_amount_without_withdraw(self):
        if self.withdraw == 0:
            self.accountblnc = self.amount + self.diposit
            return  self.accountblnc
        else:
            self.accountblnc = (self.amount + self.diposit) - self.withdraw
            return   self.accountblnc


account = Account("Nasim Haidar", "01681", 20, 50000, 1000)

print(account.getName(), account.getId())
print(account.get_payment_amount_without_withdraw())
