from database import MySQLdb
from customer_impl import CustomerImpl

class Account(CustomerImpl):

    def __init__(self, name, id, amount, diposit, withdraw):
        super(Account, self).__init__(name=name, id=id)
        self.amount = amount
        self.diposit = diposit
        self.withdraw = withdraw
        self.accountblnc=0.0

    def diposit_one(self):
         self.accountblnc = self.amount + self.diposit
         pass

    def withdraw_one(self):
        self.accountblnc = (self.amount + self.diposit) - self.withdraw
        pass

    def get_payment_amount_without_withdraw(self):
     try:
        if self.withdraw == 0:
           self.diposit_one()
           return   self.accountblnc
           
        else:
           self.withdraw_one()
           return   self.accountblnc
           
        
     except Exception as e:
        print(e)
        

account = Account("Nasim Haidar", "01681", 20, 50000, 1000)

mysql_handl = MySQLdb()
print(account.getName())
print(account.getId())
print ("Your account balance is:")
print (account.get_payment_amount_without_withdraw())
mysql_handl.show_data('customer')