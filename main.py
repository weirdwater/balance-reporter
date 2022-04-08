
from locale import format_string, setlocale, LC_NUMERIC
from balance_reporter import get_transactions, add_running_balance
from balance_reporter.balance_reporter import get_available_formats, get_format
from balance_reporter.utils import tail
import click

@click.command() # type: ignore
@click.argument('filename', type=click.Path(exists=True))
@click.option("-f", "--format", type=click.Choice(choices=list(get_available_formats())), default=None, help="The format of the statementfile")
@click.option("-b", "--balance", type=click.FLOAT, default=0.0, help="The starting balance")
def balance_report(filename: str, format: str, balance: float):
    f = get_format(format)
    if f == None:
        print("No supported format selected using --format, please choose from:")
        for name in get_available_formats():
            print("  - " + name)
        exit(1)
    transactions = get_transactions(filename, f)

    transactions_with_balance = add_running_balance(transactions, balance)

    last_balance = tail(transactions_with_balance)

    transactions_with_balance.sort(key=lambda t: t[1])
    highest_balance = tail(transactions_with_balance)

    setlocale(LC_NUMERIC, "nl")
    print("File:", filename)
    print(format_string("Number of transactions: %d", len(transactions_with_balance)))
    print(format_string("Starting balance: € %.2f", balance))
    print(format_string("Ending balance: € %.2f", last_balance[1]), "on {:%x}".format(last_balance[0].date))
    print(format_string("Highest balance: € %.2f", highest_balance[1]), "on {:%x}".format(highest_balance[0].date))

if __name__ == '__main__':
    balance_report()
