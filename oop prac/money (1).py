class Payment():
    def __init__(self, amount):
        self.amount = amount

    def paid(self):
        print(f"Paid: {self.amount}")

class Cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)

class Momo(Payment):
    def __init__(self, amount, merchantCode):
        super().__init__(amount)
        self.merchantCode = merchantCode

class Visa(Payment):
    def __init__(amount, cvc):


class Onamanja(Payment):
    def __init__(amount, contact, nationalID, address, noxtKin, witness, parents)