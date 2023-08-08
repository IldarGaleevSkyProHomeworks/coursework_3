from data_providers import data_provider
from entities import Operation
import json


class JsonFilesDataProvider(data_provider.DataProvider):

    def __init__(self, operations_file_name):
        super().__init__()

        self.__operations_file_name = operations_file_name

    def get_operations(self) -> list[Operation]:
        with open(self.__operations_file_name, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            if json_data:
                self._operations = [Operation(operation_item) for operation_item in json_data]

        return super().get_operations()
