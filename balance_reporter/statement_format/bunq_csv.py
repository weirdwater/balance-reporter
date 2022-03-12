from datetime import datetime
from .statement_format import StatementFormat
from locale import atof, setlocale, LC_NUMERIC

# Bunq follows Dutch number format
setlocale(LC_NUMERIC, "nl")

class BunqCsv(StatementFormat):

    def get_amount(self, row: list[str]) -> float:
        return atof(row[2])
    
    def get_counterparty(self, row: list[str]) -> str:
        return row[5]
    
    def get_description(self, row: list[str]) -> str:
        return row[6]
    
    def get_date(self, row: list[str]) -> datetime:
        # Bunq uses the following format for its date: YYYY-MM-DD
        return datetime.fromisoformat(row[0])


            