from coursework_3.entities import Operation


class OperationView:

    @staticmethod
    def _stringify_number(number_str: str) -> str | None:
        if number_str and number_str.isdigit():
            str_len = len(number_str)
            match str_len:
                case 16:
                    c_len = 4
                    chunks = [number_str[n:n + c_len] for n in range(0, str_len, c_len)]

                    return f"{chunks[0]} {chunks[1][:2]}XX XXXX {chunks[3]}"
                case 20:
                    return f"XX {number_str[-4:]}"

        return None

    def __init__(self, operation: Operation):
        self.__operation = operation

    @property
    def description(self) -> str:
        return self.__operation.description

    @property
    def date(self):
        return self.__operation.date.strftime('%d.%m.%Y')

    @property
    def operation_amount(self) -> str:
        return f"{round(self.__operation.operation_amount.amount, 2)} " \
               f"{self.__operation.operation_amount.currency.name}"

    @property
    def payment_from(self) -> str:
        if self.__operation.payment_from_details:
            return f"{self.__operation.payment_from_details.name} " \
                   f"{OperationView._stringify_number(self.__operation.payment_from_details.number)}"
        return "Неизвестно"

    @property
    def payment_to(self) -> str:
        if self.__operation.payment_to_details:
            return f"{self.__operation.payment_to_details.name} " \
                   f"{OperationView._stringify_number(self.__operation.payment_to_details.number)}"
        return "Неизвестно"
