import settings
from data_providers import DataProvider
from data_providers import JsonFilesDataProvider


def main(data_provider: DataProvider):
    operations_list = data_provider.get_operations()
    complete_operations = sorted([
        operation for operation in operations_list
        if operation.state == "EXECUTED"
    ], reverse=True)[:settings.SHOW_OPERATIONS_COUNT]

    for operation in complete_operations:
        print(f"{operation.date.strftime('%d.%m.%Y')} {operation.description}\n"
              f"{operation.payment_from} -> {operation.payment_to}\n"
              f"{operation.operation_amount}\n")


if __name__ == '__main__':
    data_provider = JsonFilesDataProvider(settings.OPERATIONS_DATA_FILE)
    main(data_provider)
