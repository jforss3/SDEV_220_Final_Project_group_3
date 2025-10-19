# This module contains the Order class. It creates an object for each order to store relevant info and contains methods to add or
# remove items, calculate the total price, and return a summary of the order
from menu_class import Menu
from customers_class import Customers

class Order():
    order_number = 1
    orders = {}
    
    def __init__(self, customer: Customers):
        self.customer = customer
        self.selected_items = {} # key: menu item object, value: number wanted
        self.order_id = Order.order_number
        Order.order_number += 1
        Order.orders[self.order_number] = self
    
    def __str__(self):
        order_details = ""
        order_details += f"{self.customer.get_name()}\n"
        order_details += f"order id: {self.order_id}\n"
        for item, number in self.selected_items.items():
            order_details += f"{item.name}: number ordered: {number}, subtotal: ${item.price * number:.2f}\n"
        order_details += f"Total = ${self.calculate_price():.2f}"
        return order_details

    def add_item(self, item: Menu, number: int = 1):
        if item in self.selected_items:
            self.selected_items[item] += number
        else:
            self.selected_items[item] = number

    def remove_item(self, item: Menu, number: int = None):
        if number == None or self.selected_items[item] <= number:
            del self.selected_items[item]
        else:
            self.selected_items[item] -= number
    
    def calculate_price(self):
        total = 0
        for item, number in self.selected_items.items():
            total += item.price * number
        return total
        
    def calculate_time(self):
        if "Apple Pie" in item:
            print("60 minutes")
        elif "White Cake" in item:
            print("50 minutes")
        elif "Chocolate Cookies" in item:
            print("35 minutes")
        else:
            print("0 minutes")
