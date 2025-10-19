#this is the main program witch runs the GUI

#import
#GUI handler
from breezypythongui import EasyFrame
#font
from tkinter.font import Font
from Order_class import Order
from menu_class import Menu
from customers_class import Customers

#varables
# firstName = ""
# lastName = ""
# email = ""
# address = ""
# credit = ""
#itemName = []
current_customer = None
order = None

#class
class windowLogin(EasyFrame):
    
    #init
    def __init__(self):
        EasyFrame.__init__(self, title = "Sweets Cake Bakery")
        #first title
        self.addLabel(text = "Sweets Cake Bakery", row = 0, column = 1)
        #first name input
        self.addLabel(text = "Please input your first name:", row = 3, column = 0)
        self.textFirstName = self.addTextField(text="", row = 3, column = 1, width=20)
        #last name input
        self.addLabel(text = "Please input your last name:", row = 4, column = 0)
        self.textLastName = self.addTextField(text="", row = 4, column = 1, width=20)
        #email input
        self.addLabel(text = "Please input your email:", row = 5, column = 0)
        self.textEmail = self.addTextField(text="", row = 5, column = 1, width=20)
        #address input
        self.addLabel(text = "Please input your address:", row = 6, column = 0)
        self.textAddress = self.addTextField(text="", row = 6, column = 1, width=20)
        #credit input
        self.addLabel(text = "Please input credit card:", row = 7, column = 0)
        self.textCredit = self.addTextField(text="", row = 7, column = 1, width=20)
        self.submitLoginBtn = self.addButton(text = "Submit", row = 8, column = 1, command = self.submitLoginBtn)
        self.menuBtn = self.addButton(text = "Continue to Order", row = 9, column = 1, command = self.menuBtn, state = "disable")
        self.quitBtn = self.addButton(text = "Quit", row = 10, column = 1, command = self.quitBtn)
        

    #submit the login infromation to the classes and unlocks the order button
    def submitLoginBtn(self):
        self.menuBtn["state"] = "normal"
        #global firstName
        #global lastName
        #global email
        #global address
        #global credit
        global current_customer
        #add link to customers class
        firstName = self.textFirstName.getText()
        lastName = self.textLastName.getText()
        email = self.textEmail.getText()
        address = self.textAddress.getText()
        credit = self.textCredit.getText()
        current_customer = Customers(firstName, lastName, email, address, credit)

    #opens the order window up
    def menuBtn(self):
        self.destroy()
        windowMenu()
        
    #opens the order window up
    def quitBtn(self):
        self.destroy()
        windowQuit()

#The window to add items to the order   
class windowMenu(EasyFrame):
    
    def __init__(self):
        global current_customer
        global order
        # get menu items
        with open("menu_items.txt", "rt") as menu_items:
            for item in menu_items:
                data = item.split(";")
                name = data[0]
                price = float(data[1])
                description = data[2]
                prep_time = int(data[3])
                Menu(name, price, description, prep_time)
        
        order = Order(current_customer)
        EasyFrame.__init__(self, title = "Sweets Cake Bakery")
        #first title
        self.addLabel(text = "Order Menu", row = 0, column = 1)
        self.addLabel(text = "These are the available options:", row = 1, column = 0)
        #need to add abilty to print
        self.addLabel(text = Menu.display_item_names(), row = 1, column = 1)
        self.addLabel(text = "Please input item to add:", row = 2, column = 0)
        self.textMenuAdd = self.addTextField(text="", row = 2, column = 1, width=20)
        self.includeBtn = self.addButton(text = "Add Item", row = 3, column = 1, command = self.includeBtn)
        self.removeBtn = self.addButton(text = "Remove Item", row = 4, column = 1, command = self.removeBtn)
        self.orderBtn = self.addButton(text = "Proceed to Checkout", row = 5, column = 1, command = self.orderBtn, state = "disable")
        self.quitBtn = self.addButton(text = "Quit", row = 6, column = 1, command = self.quitBtn)
        
    #add the item
    def includeBtn(self):
        #global itemName
        global order
        self.orderBtn["state"] = "normal"
        #needs to add the abilty to add items to the order.
        request = self.textMenuAdd.getText()
        if request in Menu.items:
            item = Menu.items.get(request)
            order.add_item(item)
            self.messageBox(title = "Add", message = "Your item " + request + " was added")
        else:
            self.messageBox(title = "Error", message = "Your item " + request + " is not on the menu")
    
    def removeBtn(self):
        #global itemName
        global order
        self.orderBtn["state"] = "normal"
        #needs to add the abilty to add items to the order.
        request = self.textMenuAdd.getText()
        if request in Menu.items:
            item = Menu.items.get(request)
            if item in order.selected_items:
                order.remove_item(item)
                self.messageBox(title = "Removed", message = "Your item " + request + " was removed")
            else:
                self.messageBox(title = "Error", message = "Your item " + request + " is not in the order")
        else:
            self.messageBox(title = "Error", message = "Your item " + request + " is not on the menu")

    def orderBtn(self):
        self.destroy()
        windowOrder()

    def quitBtn(self):
        self.destroy()
        windowQuit()

#The window that prints out orders
class windowOrder(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Sweets Cake Bakery")
        #first title
        self.addLabel(text = "Your Order", row = 0, column = 1)
        self.addLabel(text = "Your total come out to: ", row = 1, column = 0)
        #list the total
        self.addLabel(text = "", row = 1, column = 1)
        self.addLabel(text = "It will take about: ", row = 2, column = 0)
        #list the time it will take
        self.addLabel(text = Order.calculate_time, row = 2, column = 1)
        self.addLabel(text = "This is the customer infromation on the order: ", row = 3, column = 0)
        #List the customer infromation
        self.addLabel(text = current_customer, row = 3, column = 1)
        self.quitBtn = self.addButton(text = "Submit and Quit", row = 4, column = 1, command = self.quitBtn)
        self.menuBtn = self.addButton(text = "No, Go Back To Menu", row = 6, column = 1, command = self.menuBtn)

    def quitBtn(self):
        self.destroy()
        windowQuit()

    def menuBtn(self):
        self.destroy()
        windowMenu()

#Respone to quit
class windowQuit(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Sweets Cake Bakery")
        self.addLabel(text = "Press the 'x' in the top corner to quit", row = 0, column = 1)
  
#runs the home window
def main():
    windowLogin().mainloop()

#makes main work  
if __name__ == "__main__":
    main()

