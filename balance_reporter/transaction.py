from datetime import datetime

class Transaction(object):
    amount: float
    description: str
    counterparty: str
    date: datetime

    def __init__(self, amount: float, description: str = "", counterparty: str = "", date: datetime = datetime.now()):
        self.amount = amount
        self.description = description
        self.counterparty = counterparty
        self.date = date

    def __str__(self):
        return "Date: {self.date:%x}, Amount: {self.amount:.2f}, Counter Party: {self.counterparty}, Description: {self.description}".format(self=self)
      