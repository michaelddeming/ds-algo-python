"""Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?"""



class CreditCard:

    def __init__ (self, customer, bank, acnt, limit, override_balance=None):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

        if override_balance:
            self._balance = override_balance

    
    def charge(self, price):

        try:
            price = float(price)
        except ValueError:
            print("Price not of type: float, charge unsuccessful.")
            return False
        
        if price + self._balance > self._limit: # if charge would exceed limit,
            raise ValueError(f"{self._account} is maxed out, charge (${price}) unsuccessful")
        else:
            self._balance += price
            return True

wallet = []

wallet.append(CreditCard("John Bowman", "California Savings",
"5391 0375 9387 5309", 2500) )
wallet.append(CreditCard("John Bowman", "California Federal",
"3485 0399 3395 1954", 3500) )
wallet.append(CreditCard("John Bowman", "California Finance",
"5391 0375 9387 5309", 5000) )


for val in range(1, 100):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)
        
   
# CC 3 would exceed it's limit first. 