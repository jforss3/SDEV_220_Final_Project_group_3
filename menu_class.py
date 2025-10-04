"""

The following script contains the menu class. It creates an object for each menu item and
stores information about the menu item. The information being stored is the item's name, price,
description, and prep time

"""

class Menu:
  
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, description: str, prep_time: int):
        new_item = {
            'name': name,
            'price': price,
            'description': description,
            'prep_time': prep_time
        }
        self.items.append(new_item)
        print(f"Added: {new_item}")

    def remove_item(self, name: str):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print(f"Item '{name}' not found in the menu.")

    def display_menu(self):
        if not self.items:
            print("The menu is currently empty.")
            return
        for item in self.items:
            print(f"Item: {item['name']}, Price: ${item['price']:.2f}, Description: {item['description']}, Prep Time: {item['prep_time']} minutes")
