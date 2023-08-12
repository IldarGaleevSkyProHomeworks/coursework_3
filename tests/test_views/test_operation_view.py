from datetime import datetime

import pytest

from coursework_3.views import OperationView


@pytest.mark.parametrize("operation_amount, expected_result", [
    ((11.22, "USD"), "11.22 USD"),
    ((11, "USD"), "11.00 USD"),
    ((11.12345, "USD"), "11.12 USD"),
    ((11.00, "Руб."), "11.00 Руб."),
])
def test_operation_view_operation_amount(operation_amount, expected_result):
    operation_amount_instance = type('entities.OperationAmount',
                                     (),
                                     {
                                         "amount": operation_amount[0],
                                         "currency": type('', (object,), {
                                             "name": operation_amount[1],
                                             "code": "CUR"
                                         })
                                     })

    operation_instance = type('entities.Operation',
                              (),
                              {
                                  "operation_amount": operation_amount_instance
                              })

    instance = OperationView(operation_instance)

    assert instance.operation_amount == expected_result


@pytest.mark.parametrize("payment_details, expected_result", [
    (("SomeCard", "1111222233334444"), "SomeCard 1111 22XX XXXX 4444"),
    (("SomeBill", "11112222333344445555"), "SomeBill XX 5555"),
    (None, "Неизвестно"),
])
def test_operation_view_operation_details(payment_details, expected_result):
    payment_details_instance = None

    if payment_details:
        payment_details_instance = type('', (object,),
                                        {
                                            "name": payment_details[0],
                                            "number": payment_details[1]
                                        }
                                        )

    operation_instance = type('entities.Operation',
                              (),
                              {
                                  "payment_from_details": payment_details_instance,
                                  "payment_to_details": payment_details_instance,
                              })

    instance = OperationView(operation_instance)

    assert instance.payment_from == expected_result
    assert instance.payment_to == expected_result
