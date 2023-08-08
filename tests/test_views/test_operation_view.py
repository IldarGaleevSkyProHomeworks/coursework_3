import unittest
from datetime import datetime

from views import OperationView


class OperationViewTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._operation_instance = type('entities.Operation', (),
                                        {
                                            "id": 1234,
                                            "state": "EXECUTED",
                                            "date": datetime(2023, 8, 8),
                                            "operation_amount": type('entities.OperationAmount', (), {
                                                "amount": 123.45,
                                                "currency": type('', (object,), {
                                                    "name": "cur.",
                                                    "code": "CUR"
                                                })}),
                                            "description": "some description",
                                            "payment_from_details": type('', (object,),
                                                                         {
                                                                             "name": "Some Card",
                                                                             "number": "1111222233334444"
                                                                         }
                                                                         ),
                                            "payment_to_details": None
                                        })

    def test_operation_view__stringify_number_card_number(self):
        result = OperationView._stringify_number("1357246833331234")

        self.assertEqual(result, "1357 24XX XXXX 1234")

    def test_operation_view__stringify_number_bill_number(self):
        result = OperationView._stringify_number("12345678901234567890")

        self.assertEqual(result, "XX 7890")

    def test_operation_view_str(self):
        instance = OperationView(self._operation_instance)

        self.assertEqual(instance.date, "08.08.2023")
        self.assertEqual(instance.description, "some description")
        self.assertEqual(instance.operation_amount, "123.45 cur.")
        self.assertEqual(instance.payment_from, "Some Card 1111 22XX XXXX 4444")
        self.assertEqual(instance.payment_to, "Неизвестно")
