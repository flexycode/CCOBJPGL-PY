from Junkfood import Junkfood
from Shampoo import Shampoo
from Cashier import Cashier

def main():
    # Polymorphic variable/object
    item1 = Junkfood()
    item1.name = "Piatos"

    # Polymorphic variable/object
    item2 = Shampoo()
    item2.name = "SunSilk"

    # Polymorphic list
    item_list = [item1, item2]

    # Instead of calling the show_item_name for each grocery item, we can loop
    # through the polymorphic list
    for item in item_list:
        item.show_item_name()

    # Cashier Object
    c1 = Cashier()

    # Polymorphic Argument
    c1.check_out(item1)

    # Polymorphic Argument
    c1.check_out(item2)

if __name__ == "__main__":
    main()