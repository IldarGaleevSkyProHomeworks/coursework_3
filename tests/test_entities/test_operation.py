import unittest
from entities import Operation


class OperationTestCase(unittest.TestCase):

    def test_operation__parse_bill_number_correct(self):

        result_bill_details = Operation._parse_payment_details("Счет 12345678901234567890")
        result_card_details = Operation._parse_payment_details("Some Card 1111222233334444")

        self.assertEqual(result_bill_details.number, "12345678901234567890")
        self.assertEqual(result_bill_details.name, "Счет")

        self.assertEqual(result_card_details.number, "1111222233334444")
        self.assertEqual(result_card_details.name, "Some Card")

    def test_operation__parse_bill_number_invalid(self):

        result_1 = Operation._parse_payment_details("Счет 1234567890123")
        result_2 = Operation._parse_payment_details("")

        self.assertIsNone(result_1)
        self.assertIsNone(result_2)

    def test_operation__stringify_number_card_number(self):

        result = Operation._stringify_number("1357246833331234")

        self.assertEqual(result, "1357 24XX XXXX 1234")

    def test_operation__stringify_number_bill_number(self):

        result = Operation._stringify_number("12345678901234567890")

        self.assertEqual(result, "XX 7890")


if __name__ == '__main__':
    unittest.main()
