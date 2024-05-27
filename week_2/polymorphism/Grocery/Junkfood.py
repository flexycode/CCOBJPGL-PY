from GroceryItem import GroceryItem

class Junkfood(GroceryItem):
    def show_item_name(self):
        print(f"The name of this junkfood is {self.name}")