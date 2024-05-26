from Person import Person

def main():
    me = Person()

    # The name property cannot be accessed directly from outside the class.
    # me.__name

    me.set_name("Jay")