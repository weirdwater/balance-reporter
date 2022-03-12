from datetime import datetime
from .statement_format import StatementFormat
from locale import atof, setlocale, LC_NUMERIC

# ING uses Dutch number format
setlocale(LC_NUMERIC, "nl")

class IngCsv(StatementFormat):

    def get_amount(self, row: list[str]) -> float:
        amount = atof(row[6])
        # ING uses a discriminator for determining the mutation type
        debitorcredit = row[5]
        if debitorcredit == "Debit":
            amount *= -1
        return amount
    
    def get_counterparty(self, row: list[str]) -> str:
        return row[1]
    
    def get_description(self, row: list[str]) -> str:
        return row[8]
    
    def get_date(self, row: list[str]) -> datetime:
        # ING uses the following format for its date: YYYYMMDD

        date = row[0] 
        year  = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])

        return datetime(year, month, day)


            