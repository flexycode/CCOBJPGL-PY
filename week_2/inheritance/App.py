from Son import Son
from Daughter import Daughter

def main():
    # Son object
    me = Son()
    me.name = "Jay Arre"

    # The Son class inherited the surname attribute and the get_surname() method
    surname = me.get_surname()

    print(f"My name is {me.name} and my surname is {surname}")

    # Daughter object
    my_sister = Daughter()
    my_sister.name = "Dianne"

    # The Daughter class also inherited the surname attribute and the get_surname() method
    surname = my_sister.get_surname()

    print(f"My sister's name is {my_sister.name} and her surname is also {surname}")

if __name__ == "__main__":
    main()