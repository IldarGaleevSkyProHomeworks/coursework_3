import pytest
from coursework_3.entities import Operation
from coursework_3.entities import OperationAmount
from datetime import datetime


@pytest.mark.parametrize("input_str, expected_result", [
    ("BillNumber 12345678901234567890", ("BillNumber", "12345678901234567890")),
    ("Some Card 1111222233334444", ("Some Card", "1111222233334444")),
])
def test_operation__from_to(fixture_datetime, input_str, expected_result):
    instance = Operation({"date": fixture_datetime[0], "from": input_str, "to": input_str})

    assert instance.payment_from_details == expected_result
    assert instance.payment_to_details == expected_result


@pytest.mark.parametrize("input_str", [
    "",
    None,
    "Bill 1234",
    "Some card 1111222233334444555566667777"
])
def test_operation__from_to_invalid(fixture_datetime, input_str):
    instance = Operation({"date": fixture_datetime[0], "from": input_str, "to": input_str})

    assert instance.payment_to_details is None
    assert instance.payment_from_details is None


def test_operation__all_properties_valid(fixture_datetime):

    operation_item = {
        "id": 1234,
        "state": "EXECUTED",
        "date": fixture_datetime[0],
        "operationAmount": {
            "amount": "123.45",
            "currency": {
                "name": "cur.",
                "code": "CUR"
            }
        },
        "description": "some description",
    }

    instance = Operation(operation_item)

    assert instance.state == "EXECUTED"
    assert instance.date == fixture_datetime[1]
    assert instance.operation_amount == OperationAmount({"amount": "123.45", "currency": {"code": "CUR"}})
    assert instance.description == "some description"


def test_operation__less():
    instance_1 = Operation({
        "date": "2023-08-08T15:16:16.0"
    })

    instance_2 = Operation({
        "date": "2023-08-09T15:16:16.0"
    })

    date_time = datetime(2023, 8, 15)

    assert instance_1 < instance_2
    assert instance_1 < date_time


def test_operation__less_raise():
    instance_1 = Operation({"date": "2023-08-08T15:16:16.0"})

    with pytest.raises(TypeError):
        _ = instance_1 < 1234
