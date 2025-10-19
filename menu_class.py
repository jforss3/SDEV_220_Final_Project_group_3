"""

The following script contains the menu class. It stores each item's info as object attributes and contains a dictionary with all of
the objects. The information being stored is the item's name, price, description, and prep time

"""

class Menu:
    items = {}

    def __init__(self, name: str, price: float, description: str, prep_time: int):
        self.name = name
        self.price = price
        self.description = description
        self.prep_time = prep_time
        Menu.items[self.name] = self

    @classmethod
    def remove_item(cls, name: str):
        if name in Menu.items:
            del Menu.items[name]
        else:
            print(f"Item '{name}' not found in the menu.")

    @classmethod
    def display_menu(cls):
        if not Menu.items:
            return "The menu is currently empty."
        item_string = ""
        for item in Menu.items.values():
            item_string += f"Item: {item.name}, Price: ${item.price:.2f}, Description: {item.description}, Prep Time: {item.prep_time} minutes\n"
    
    @classmethod
    def display_item_names(cls):
        if not Menu.items:
            return "The menu is currently empty."
        #item_string = ""
        #for item in Menu.items.keys():
        return ", ".join(Menu.items.keys())