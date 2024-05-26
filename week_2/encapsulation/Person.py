class Person:
    def __init__(self):
        self.__name = None  # Private variable (name mangled to _Person__name)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name