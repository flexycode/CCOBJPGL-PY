from Mango import Mango
from Strawberry import Strawberry
from Banana import Banana

def main():
    # Mango object
    philippine_mango = Mango()
    philippine_mango.color = "Bright Yellow"
    philippine_mango.taste = "Very Sweet"
    philippine_mango.show_color_and_taste()

    # Strawberry object
    white_goblin = Strawberry()
    white_goblin.color = "white"
    white_goblin.taste = "Sweet and Sour"
    white_goblin.show_color_and_taste()

    # Banana object
    lacatan = Banana()
    lacatan.color = "Yellow"
    lacatan.taste = "Sweet"
    lacatan.show_color_and_taste()

if __name__ == "__main__":
    main()