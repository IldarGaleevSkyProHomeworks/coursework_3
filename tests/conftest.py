from datetime import datetime

import pytest


@pytest.fixture
def fixture_datetime():
    return "2023-08-08T15:16:16.0", datetime(2023, 8, 8, 15, 16, 16)
