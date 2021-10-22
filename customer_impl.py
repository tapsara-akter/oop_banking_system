from customer import Customer


class CustomerImpl(Customer):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id


# student Implementation class object
#customer = CustomerImpl("Tarek", "01861")
#print(customer.name, customer.id)
#print(customer.getName())
#print(customer.getId())