#This is the customers class

class Customers():
    id_Num = 1
    customer_dict = {}
    def __init__(self, first_name, last_name, email, address, credit_card):
        self.customer_id = Customers.id_Num
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.credit_card = credit_card
        Customers.id_Num += 1
        Customers.customer_dict[self.customer_id] = self
    
    def get_name(self):
        return f"{self.first_name} {self.last_name}"