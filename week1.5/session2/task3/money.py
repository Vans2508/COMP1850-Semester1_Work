# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence:02d}"  # Format pence with leading zero if needed
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        if not isinstance(other, Money): #if the other object is not a Money object, raise a TypeError
            raise TypeError("Can only add Money to Money")
    
        # add self to other, then return the sum as a new Money object
        else: #if it is a Money object, add the pounds and pence together, and return a new Money object with the total
            total_pounds = self.pounds + other.pounds #add the pounds
            total_pence = self.pence + other.pence #add the pence
            if total_pence >= 100: #if the total pence is greater than or equal to 100, convert it to pounds and pence
                total_pounds += total_pence // 100 #add the number of pounds to the total pounds
                total_pence = total_pence % 100 #set the total pence to the remainder of the division by 100
            return Money(total_pounds, total_pence) #return a new Money object with the total pounds and pence

        # (see README for hints and tips)
