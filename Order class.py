# This module contains the Order class. It creates an object for each order to store relevant info and contains methods to add or
# remove items, calculate the total price, and return a summary of the order

class Order():
    order_number = 1
    
    def __init__(self, customer):
        self.customer = customer
        self.selected_items = {} # key: menu item object, value: number wanted
        self.order_id = Order.order_number
        Order.order_number += 1
    
    def __str__(self):
        order_details = ""
        order_details += f"{self.customer.name}\n"
        order_details += f"order id: {self.order_id}\n"
        for item, number in self.selected_items.items():
            order_details += f"{item.name}: number ordered: {number}, subtotal: ${item.price * number:.2f}\n"
        order_details += f"Total = ${self.calculate_price():.2f}"
        return order_details

    def add_item(self, item, number = 1):
        if item in self.selected_items:
            self.selected_items[item] += number
        else:
            self.selected_items[item] = number

    def remove_item(self, item, number = None):
        if number == None or self.selected_items[item] <= number:
            del self.selected_items[item]
        else:
            self.selected_items[item] -= number
    
    def calculate_price(self):
        total = 0
        for item, number in self.selected_items.items():
            total += item.price * number
        return total