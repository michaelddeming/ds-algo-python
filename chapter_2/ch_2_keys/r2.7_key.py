"""The CreditCard class of Section 2.3 initializes the balance of a new ac-
count to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance."""



class CreditCard:

    def __init__ (self, customer, bank, acnt, limit, override_balance=None):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

        if override_balance:
            self._balance = override_balance

    def get_balance(self):
        print(self._balance)


cc1 = CreditCard("Kitty", "Keybank", 123, 1000)
cc2 = CreditCard("Michael", "Chase", 456, 1000, override_balance=500)


cc1.get_balance()
cc2.get_balance()
