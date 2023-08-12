from os import path

from coursework_3.data_providers import JsonFilesDataProvider

TEST_DIR = path.join(path.dirname(__file__), '..')


def test_json_files_data_provider():
    file_name = path.join(TEST_DIR, "test_data", "operations_test_data.json")
    instance = JsonFilesDataProvider(file_name)

    var = instance.get_operations()

    assert len(var) == 3
    assert var[0].description == "First operation"
