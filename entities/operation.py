import re
from collections import namedtuple


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
