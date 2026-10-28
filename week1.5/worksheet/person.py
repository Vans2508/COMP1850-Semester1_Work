# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        self.name = name
        self.birth = birth

        if not isinstance(name, (str)):
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name cannot be empty")
        if not isinstance(birth, (date)):
            raise TypeError("The date of birth is not valid")

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        words = self.name.split()
        return
    def is_birthday(self):
        return self.birth.date() == date.today()
