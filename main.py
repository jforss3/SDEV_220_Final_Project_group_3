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
firstName = ""
lastName = ""
email = ""
address = ""
credit = ""

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
        global firstName
        global lastName
        global email
        global address
        global credit
        #add link to customers class
        firstName = self.textFirstName.getText()
        lastName = self.textLastName.getText()
        email = self.textEmail.getText()
        address = self.textAddress.getText()
        credit = self.textCredit.getText()

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
        # simulates reading menu data from a text file
        menuList = {
            "name": ["Apple Pie", "White Cake", "Chocolate Cookies"],
            "price": [10.00, 15.00, 5.00],
            "description": ["Freshly baked apple pie from fresh apples from the local farm.",
                            "White cake made from a generation-defining recipe.",
                            "Chocolate cookies made with chocolate by our local chocolatier Alex."],
            "prep_time": [60, 50, 35]}
        for i in range(len(menuList["name"])):
            name = menuList["name"][i]
            price = menuList["price"][i]
            description = menuList["description"][i]
            prep_time = menuList["prep_time"][i]
            Menu(name, price, description, prep_time)
            
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
        self.orderBtn["state"] = "normal"
        #needs to add the abilty to add items to the order.
    
    def removeBtn(self):
        self.orderBtn["state"] = "normal"
        #need to add the abilty to remove items

    def orderBtn(self):
        self.destroy()
        windowOrder()

    def quitBtn():
        pass

#The window that prints out orders
class windowOrder(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Your Order")
        #first title
        self.addLabel(text = "Order", row = 0, column = 1)
        #needs to code the ending part.

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
