import csv
from .transaction import Transaction
from .statement_format import StatementFormat

def get_transactions(filename: str, format: StatementFormat) -> list[Transaction]:
    transactions: list[Transaction] = []

    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__() # Skip the header
        for row in reader:
            t = format.to_transaction(row)
            transactions.append(t)

    return transactions

def add_running_balance(transactions: list[Transaction], starting_balance: float = 0.0) -> list[tuple[Transaction, float]]:
    transactions_with_balance: list[tuple[Transaction, float]] = []

    transactions.sort(key=lambda t : t.date)
    for i, t in enumerate(transactions):
        prevBalance = transactions_with_balance[i - 1][1] if i > 0 else starting_balance
        transactions_with_balance.append((t, prevBalance + t.amount))

    return transactions_with_balance