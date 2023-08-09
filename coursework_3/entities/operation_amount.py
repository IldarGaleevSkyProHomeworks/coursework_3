from typing import NamedTuple


class OperationCurrency(NamedTuple):
    """ Represents information about the currency """
    name: str
    code: str


class OperationAmount:
    """ Represents information about the operation amount """

    def __init__(self, operation_amount: dict | None):
        if not operation_amount:
            operation_amount = {}

        self._amount = float(operation_amount.get("amount", "0.0"))
        currency = operation_amount.get("currency", {"name": None, "code": None})
        currency_name = currency.get("name", None)
        currency_code = currency.get("code", None)
        self._currency = OperationCurrency(name=currency_name, code=currency_code)

    @property
    def amount(self) -> float:
        """ Operation amount """
        return self._amount

    @property
    def currency(self) -> OperationCurrency:
        """ Information about the operation currency """
        return self._currency

    def __float__(self):
        return self._amount

    def __str__(self):
        return f"{round(self._amount, 2)} {self._currency.name}"

    def __repr__(self):
        return f"{self.__class__.__name__} (" \
               f"amount={self._amount}, " \
               f"currency={self._currency}" \
               f")"

    def __eq__(self, other):
        if type(other) is OperationAmount:
            return self._amount == other._amount and self._currency.code.lower() == other._currency.code.lower()
        return False
