import unittest
import unittest.mock
from datetime import datetime

from data_providers import DataProvider


class DataProviderTestCase(unittest.TestCase):
    class DataProviderTestClass(DataProvider):
        def __init__(self):
            super().__init__()
            self._operations = [
                type('entities.Operation', (), {
                    'date': datetime(2023, 1, 1),
                    'state': 'EXECUTED',
                    'payment_from_details': type('', (object,), {
                        'name': 'Card',
                        'number': '1111222233334441'
                    }),
                    'payment_to_details': type('', (object,), {
                        'name': 'Card',
                        'number': '1111222233334442'
                    })}),

                type('entities.Operation', (), {
                    'date': datetime(2023, 1, 2),
                    'state': 'CANCELED',
                    'payment_from_details': type('', (object,), {
                        'name': 'Card',
                        'number': '1111222233334441'
                    }),
                    'payment_to_details': type('', (object,), {
                        'name': 'Card',
                        'number': '1111222233334443'
                    })}),

                type('entities.Operation', (), {
                    'date': datetime(2023, 1, 3),
                    'state': 'EXECUTED',
                    'payment_from_details': type('', (object,), {
                        'name': 'Card',
                        'number': '1111222233334443'
                    }),
                    'payment_to_details': type('', (object,), {
                        'name': 'Card',
                        'number': '1111222233334442'
                    })}),
            ]

    def test_data_provider_get_operations(self):
        instance = DataProviderTestCase.DataProviderTestClass()
        lst = instance.get_operations()
        self.assertEqual(len(lst), 3)

    def test_data_provider_get_account_operations(self):
        instance = DataProviderTestCase.DataProviderTestClass()
        lst = instance.get_operations_by_account_number('1111222233334441')
        self.assertEqual(len(lst), 2)


if __name__ == '__main__':
    unittest.main()
