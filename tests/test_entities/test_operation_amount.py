from coursework_3.entities import OperationAmount


def test_operation_amount__all_properties_valid():
    operation_amount_item = {
        "amount": "12345.67",
        "currency": {
            "name": "вал.",
            "code": "CUR"
        }
    }

    instance = OperationAmount(operation_amount_item)

    assert instance.amount == 12345.67
    assert instance.currency.code == "CUR"
    assert instance.currency.name == "вал."


def test_operation_amount__all_properties_invalid():
    operation_amount_item = None

    instance = OperationAmount(operation_amount_item)

    assert instance.amount == 0.0
    assert instance.currency.code is None
    assert instance.currency.name is None


def test_operation_amount__is_equal():
    instance_1 = OperationAmount({"amount": "1234", "currency": {"code": "Usd"}})
    instance_2 = OperationAmount({"amount": "1234", "currency": {"code": "USD"}})

    assert instance_1 == instance_2


def test_operation_amount__is_not_equal():
    instance_1 = OperationAmount({"amount": "1234.5", "currency": {"code": "Usd"}})
    instance_2 = OperationAmount({"amount": "1234.5", "currency": {"code": "RUB"}})
    instance_3 = OperationAmount({"amount": "123.4", "currency": {"code": "USD"}})
    instance_4 = 1234.5

    assert not instance_1 == instance_2
    assert not instance_1 == instance_3
    assert not instance_1 == instance_4
