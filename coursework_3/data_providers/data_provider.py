from coursework_3.entities import Operation


class DataProvider:
    """Data provider base class"""

    def __init__(self):
        self._operations = []

    def get_operations(self) -> list[Operation]:
        """Get all operations list"""

        return self._operations

    def get_operations_by_status(self, operation_status: str):
        """
        Get operations by status
        :param operation_status: Operation status (EXECUTE, CANCELED)
        :return: Filtered operations
        """
        return [
                    operation for operation in self._operations
                    if operation.state == operation_status
                ]

    def __str__(self):
        return '\n'.join([str(item) for item in self._operations])

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"operations={self._operations.__repr__()}" \
               f")"
