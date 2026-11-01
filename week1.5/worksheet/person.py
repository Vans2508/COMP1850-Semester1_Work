# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        """
        Creates a Person class initalising it with a name and a birth date 
        """
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
        """
        Returns the initials of the person
        """
        words = self.name.split()
        return "".join([name[0].upper() for name in words])
    def is_birthday(self):
        """
        Returns true if today is the person's birthday based on their birth date
        """
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day