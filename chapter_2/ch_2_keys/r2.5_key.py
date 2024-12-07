"""Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter."""

def charge(self, price):

    try:
        price = float(price)
    except ValueError:
        print("Price not of type: float, charge unsuccessful.")
        return False
    
    if price + self.balance > self.limit: # if charge would exceed limit,
        return False # cannot accept charge
    else:
        self.balance += price
        return True

def make_payment(self, amount):
    try:
        amount = float(amount)
    except ValueError:
        print("Amount not of type: float, payment unsuccessful")
        return False
    
    self.balance -= amount
    