
from locale import format_string, setlocale, LC_NUMERIC
from balance_reporter import get_transactions, add_running_balance
from balance_reporter.statement_format import StatementFormat, BunqCsv
from balance_reporter.utils import tail

filename: str = "bunq-statement.csv"
format: StatementFormat = BunqCsv()
starting_balance = 0.0

try:
    transactions = get_transactions(filename, format)
except FileNotFoundError:
    exit("File does not exist")
except Exception as e:
    print("Something went wrong parsing the transactions", e)
    exit(1)
    

transactions_with_balance = add_running_balance(transactions, starting_balance)

last_balance = tail(transactions_with_balance)

transactions_with_balance.sort(key=lambda t: t[1])
highest_balance = tail(transactions_with_balance)

setlocale(LC_NUMERIC, "nl")
print("File:", filename)
print(format_string("Number of transactions: %d", len(transactions_with_balance)))
print(format_string("Starting balance: € %.2f", starting_balance))
print(format_string("Ending balance: € %.2f", last_balance[1]), "on {:%x}".format(last_balance[0].date))
print(format_string("Highest balance: € %.2f", highest_balance[1]), "on {:%x}".format(highest_balance[0].date))
