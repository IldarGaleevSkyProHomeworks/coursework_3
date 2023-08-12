from typing import NamedTuple
from datetime import datetime

from coursework_3.entities import operation_amount


class Operation:
    """
    Represents operation details
    """

    class PaymentDetails(NamedTuple):
        """ Represents payment details: name and bill/card number """
        name: str
        number: str

    @staticmethod
    def _parse_payment_details(incoming_str: str) -> PaymentDetails | None:
        """
        Extract payment details from string
        :param incoming_str: string with payment details
        :return: named tuple with a name and  card/bill number, None for invalid string
        """

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
        """
        Information about the sender of the payment
        :return: PaymentDetails object
        """
        return self._from

    @property
    def payment_to_details(self) -> PaymentDetails | None:
        """
        Information about the payment recipient
        :return: PaymentDetails object
        """
        return self._to

    @property
    def state(self) -> str:
        """
        Operation state
        :return: EXECUTED, CANCELED
        """
        return self._state

    @property
    def date(self) -> datetime:
        """
        Operation datetime
        :return:
        """
        return self._date

    @property
    def operation_amount(self) -> operation_amount.OperationAmount:
        """
        Information about amount and currency
        :return: OperationAmount object
        """
        return self._operation_amount

    @property
    def description(self) -> str:
        """
        Operation description
        :return:
        """
        return self._description
