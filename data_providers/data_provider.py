from entities import Operation


class DataProvider:
    """Data provider base class"""

    def __init__(self):
        self._operations = []

    def get_operations(self) -> list[Operation]:
        """Get all operations list"""

        return self._operations

    def get_operations_by_account_number(self, account_number: str):
        """
        Get operations for account
        :param account_number: card or bill number
        :return:
        """

        account_number = account_number.replace(' ', '')
        if not account_number.isdigit() or not(len(account_number) in [16, 20]):
            raise ValueError(f"\"{account_number}\" is not a valid account number")

        return [
            operation_item for
            operation_item in self.get_operations()
            if operation_item.payment_to_details.number == account_number or
               operation_item.payment_from_details.number == account_number
        ]

    def __str__(self):
        return '\n'.join([str(item) for item in self._operations])

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"operations={self._operations.__repr__()}" \
               f")"
