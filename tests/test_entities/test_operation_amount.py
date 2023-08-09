import unittest
from coursework_3.entities import OperationAmount


class OperationAmountTestCase(unittest.TestCase):
    def test_operation_amount__all_properties_valid(self):
        operation_amount_item = {
            "amount": "12345.67",
            "currency": {
                "name": "вал.",
                "code": "CUR"
            }
        }

        instance = OperationAmount(operation_amount_item)

        self.assertEqual(instance.amount, 12345.67)
        self.assertEqual(instance.currency.code, "CUR")
        self.assertEqual(instance.currency.name, "вал.")

    def test_operation_amount__all_properties_invalid(self):
        operation_amount_item = None

        instance = OperationAmount(operation_amount_item)

        self.assertEqual(instance.amount, 0.0)
        self.assertIsNone(instance.currency.code)
        self.assertIsNone(instance.currency.name)

    def test_operation_amount__is_equal(self):
        instance_1 = OperationAmount({"amount": "1234", "currency": {"code": "Usd"}})
        instance_2 = OperationAmount({"amount": "1234", "currency": {"code": "USD"}})

        self.assertEqual(instance_1, instance_2)

    def test_operation_amount__is_not_equal(self):
        instance_1 = OperationAmount({"amount": "1234.5", "currency": {"code": "Usd"}})
        instance_2 = OperationAmount({"amount": "123.4", "currency": {"code": "USD"}})
        instance_3 = OperationAmount({"amount": "1234.5", "currency": {"code": "RUB"}})
        instance_4 = 1234.5

        self.assertNotEqual(instance_1, instance_2)
        self.assertNotEqual(instance_1, instance_3)
        self.assertNotEqual(instance_1, instance_4)
