import re
from collections import namedtuple
from datetime import datetime

from entities import operation_amount


class Operation:

    PaymentDetails = namedtuple("PaymentDetails", "name number")

    @staticmethod
    def _parse_payment_details(incoming_str: str) -> PaymentDetails | None:
        if incoming_str:
            pattern = r"^((?P<name>.+)\s)?(?P<number>\d{16}|\d{20})$"
            match = re.search(pattern, incoming_str)
            if match:
                return Operation.PaymentDetails(name=match.group("name"), number=match.group("number"))

        return None

    @staticmethod
    def _stringify_number(number_str: str) -> str | None:
        if number_str and number_str.isdigit():
            str_len = len(number_str)
            match str_len:
                case 16:
                    c_len = 4
                    chunks = [number_str[n:n+c_len] for n in range(0, str_len, c_len)]

                    return f"{chunks[0]} {chunks[1][:2]}XX XXXX {chunks[3]}"
                case 20:
                    return f"XX {number_str[-4:]}"

        return None

    def __init__(self, operation_details: dict):
        self._id = operation_details.get("id", 0)
        self._date = datetime.strptime(operation_details.get("date", ""), "%Y-%m-%dT%H:%M:%S.%f")
        self._state = operation_details.get("state", None)
        self._operation_amount = operation_amount.OperationAmount(operation_details.get("operationAmount", None))
        self._description = operation_details.get("description", None)
        self._from = Operation._parse_payment_details(operation_details.get("from", None))
        self._to = Operation._parse_payment_details(operation_details.get("to", None))

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self._id}," \
               f"date={self._date},"\
               f"state={self._state}," \
               f"operationAmount={self._operation_amount}," \
               f"description={self._description}," \
               f"from={self._from}," \
               f"to={self._to}" \
               f")"

    @property
    def payment_from(self):
        if self._from:
            return f"{self._from.name} {Operation._stringify_number(self._from.number)}"
        return None

    @property
    def payment_from_details(self) -> PaymentDetails | None:
        return self._from

    @property
    def payment_to(self):
        if self._to:
            return f"{self._to.name} {Operation._stringify_number(self._to.number)}"
        return None

    @property
    def payment_to_details(self) -> PaymentDetails | None:
        return self._to

    @property
    def state(self) -> str:
        return self._state

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def operation_amount(self) -> operation_amount.OperationAmount:
        return self._operation_amount

    @property
    def description(self) -> str:
        return self._description
