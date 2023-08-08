import unittest
from os import path

from data_providers import JsonFilesDataProvider


class JsonFilesDataProviderTestCase(unittest.TestCase):
    TEST_DIR = path.join(path.dirname(__file__), '..')

    def test_json_files_data_provider(self):
        file_name = path.join(JsonFilesDataProviderTestCase.TEST_DIR, "test_data", "operations_test_data.json")
        instance = JsonFilesDataProvider(file_name)
        var = instance.get_operations()
        self.assertEqual(len(var), 3)
        self.assertEqual(var[0].description, "First operation")


if __name__ == '__main__':
    unittest.main()
