from collections import namedtuple
from datetime import datetime

from entities import operation_amount


class Operation:

    PaymentDetails = namedtuple("PaymentDetails", "name number")

    @staticmethod
    def _parse_payment_details(incoming_str: str) -> PaymentDetails | None:
        if incoming_str:
            chunks = incoming_str.split()

            if chunks:
                name = ' '.join(chunks[:-1])
                number = chunks[-1]

                if number.isdigit() and (len(number) in [16, 20]):
                    return Operation.PaymentDetails(name=name, number=number)

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

    def __lt__(self, other):
        match other:
            case datetime():
                return self.date < other
            case Operation():
                return self.date < other.date
            case _:
                raise TypeError("Compare type error: the second operator must be Operation or datetime.")

    @property
    def payment_from_details(self) -> PaymentDetails | None:
        return self._from

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
