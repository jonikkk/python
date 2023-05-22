import unittest
import os
import json
from tempfile import NamedTemporaryFile
from Home_work_10_v2 import FileStorage, Pagination, App



class FileStorageTests(unittest.TestCase):
    def setUp(self):
        self.temp_file = NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_save_to_file(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        file_storage = FileStorage(data)
        file_storage.save_to_file(self.temp_file.name)

        with open(self.temp_file.name, 'r') as f:
            saved_data = json.load(f)

        self.assertEqual(saved_data, data)

    def test_load_from_file(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        with open(self.temp_file.name, 'w') as f:
            json.dump(data, f)

        file_storage = FileStorage.load_from_file(self.temp_file.name)
        loaded_data = file_storage.data

        self.assertEqual(loaded_data, data)

    def test_get_courses_name(self):
        data = {'Python basic': 'value1', 'Python pro': 'value2'}
        with open(self.temp_file.name, 'w') as f:
            json.dump(data, f)

        file_storage = FileStorage.load_from_file(self.temp_file.name)
        keys = list(file_storage.data.keys())

        self.assertEqual(keys, ['Python basic', 'Python pro'])


class PaginationTests(unittest.TestCase):
    def test_pagination(self):
        data = [1, 2, 3, 4]
        pagination = Pagination(data, items_per_page=3)

        page_data = pagination.get_current_page_data()
        self.assertEqual(page_data, [1, 2, 3])

        pagination.next_page()
        page_data = pagination.get_current_page_data()
        self.assertEqual(page_data, [4])

        pagination.next_page()
        page_data = pagination.get_current_page_data()
        self.assertEqual(page_data, [])

        pagination.previous_page()
        page_data = pagination.get_current_page_data()
        self.assertEqual(page_data, [4])


class AppTests(unittest.TestCase):
    def test_add_student(self):
        file_storage = FileStorage({})
        app = App(file_storage)
        app.add_course()
        app.add_student()
        expected_data = {'Python basic': ['John Dow']}
        self.assertEqual(app.file_storage.data, expected_data)



if __name__ == '__main__':
    unittest.main()
