"""If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent"""


def make_payment(self, amount):
    try:
        amount = float(amount)
    except ValueError:
        print("Amount not of type: float, payment unsuccessful")
        return False
    
    #check for negative amount given by user.
    if amount < 0:
        raise ValueError("Amount cannot be negative, payment unsuccessful")

    
    self.balance -= amount
    
    

