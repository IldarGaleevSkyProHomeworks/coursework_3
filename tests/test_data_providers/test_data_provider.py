import unittest.mock
from datetime import datetime

import pytest

from coursework_3.data_providers import DataProvider


class DataProviderTestClass(DataProvider):
    """ Some DataProvider implementation """

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


@pytest.fixture()
def fixture_dataprovider_instance():
    return DataProviderTestClass()


def test_data_provider_get_operations(fixture_dataprovider_instance):
    lst = fixture_dataprovider_instance.get_operations()

    assert len(lst) == 3


def test_data_provider_get_account_operations(fixture_dataprovider_instance):
    lst = fixture_dataprovider_instance.get_operations_by_account_number('1111222233334441')

    assert len(lst) == 2


@pytest.mark.parametrize("operation_status, expected_result", [
    ("CANCELED", 1),
    ("EXECUTED", 2),
    ("UNKNOWN", 0)
])
def test_data_provider_get_operations_by_status(fixture_dataprovider_instance, operation_status, expected_result):
    lst = fixture_dataprovider_instance.get_operations_by_status(operation_status)

    assert len(lst) == expected_result
