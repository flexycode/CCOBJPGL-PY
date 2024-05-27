from GroceryItem import GroceryItem

class Shampoo(GroceryItem):
    def show_item_name(self):
        print(f"The name of this shampoo is {self.name}")