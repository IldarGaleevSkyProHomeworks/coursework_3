import settings
from data_providers import DataProvider
from data_providers import JsonFilesDataProvider
from views import OperationView


def main(data_provider: DataProvider):
    operations_list = data_provider.get_operations()
    complete_operations = sorted([
        operation for operation in operations_list
        if operation.state == "EXECUTED"
    ], reverse=True)[:settings.SHOW_OPERATIONS_COUNT]

    operation_view_list = [OperationView(operation) for operation in complete_operations]

    for operation in operation_view_list:
        print(f"{operation.date} {operation.description}\n"
              f"{operation.payment_from} -> {operation.payment_to}\n"
              f"{operation.operation_amount}\n")


if __name__ == '__main__':
    data_provider = JsonFilesDataProvider(settings.OPERATIONS_DATA_FILE)
    main(data_provider)
