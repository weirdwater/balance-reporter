from abc import ABC, abstractmethod
from datetime import datetime
from ..transaction import Transaction

class StatementFormat(ABC):

    @abstractmethod
    def get_amount(self, row: list[str]) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_description(self, row: list[str]) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_counterparty(self, row: list[str]) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_date(self, row: list[str]) -> datetime:
        raise NotImplementedError()

    def to_transaction(self, row: list[str]) -> Transaction:
        return Transaction(self.get_amount(row), self.get_description(row), self.get_counterparty(row), self.get_date(row))
