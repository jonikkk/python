import os
import json
import pytest
from tempfile import NamedTemporaryFile
from Home_work_10_v3 import FileStorage, Pagination, App


@pytest.fixture
def temp_file():
    temp_file = NamedTemporaryFile(delete=False)
    yield temp_file.name
    os.remove(temp_file.name)


def test_save_to_file(temp_file):
    data = {'key1': 'value1', 'key2': 'value2'}
    file_storage = FileStorage(data)
    file_storage.save_to_file(temp_file)

    with open(temp_file, 'r') as f:
        saved_data = json.load(f)

    assert saved_data == data


def test_load_from_file(temp_file):
    data = {'key1': 'value1', 'key2': 'value2'}
    with open(temp_file, 'w') as f:
        json.dump(data, f)

    file_storage = FileStorage.load_from_file(temp_file)
    loaded_data = file_storage.data

    assert loaded_data == data


def test_get_courses_name(temp_file):
    data = {'Python basic': 'value1', 'Python pro': 'value2'}
    with open(temp_file, 'w') as f:
        json.dump(data, f)

    file_storage = FileStorage.load_from_file(temp_file)
    keys = list(file_storage.data.keys())

    assert keys == ['Python basic', 'Python pro']


def test_pagination():
    data = [1, 2, 3, 4]
    pagination = Pagination(data, items_per_page=3)

    page_data = next(pagination)
    assert page_data == [1, 2, 3]

    pagination.next_page()
    page_data = next(pagination)
    assert page_data == [4]

    pagination.next_page()
    with pytest.raises(StopIteration):
        next(pagination)

    pagination.previous_page()
    page_data = next(pagination)
    assert page_data == [4]


def test_add_student(capfd):
    file_storage = FileStorage({})
    app = App(file_storage)
    app.add_course()
    app.add_student()
    expected_data = {'Python basic': ['John Dow']}
    assert app.file_storage.data == expected_data

    out, _ = capfd.readouterr()
    assert "Course 'Python basic' added." in out
    assert "Student John Dow added to Course Python basic." in out


def test_remove_course(capfd):
    data = {'Python basic': [], 'Python pro': []}
    file_storage = FileStorage(data)
    app = App(file_storage)

    app.remove_course()
    assert app.file_storage.data == data

    out, _ = capfd.readouterr()
    assert "Enter course name to remove: " in out
    assert "Course 'Python basic' removed." in out

    app.remove_course()
    assert app.file_storage.data == {}

    out, _ = capfd.readouterr()
    assert "Enter course name to remove: " in out
    assert "Course 'Python pro' removed." in out


def test_remove_student(capfd):
    data = {'Python basic': ['John Doe', 'Jane Smith', 'John Smith'], 'Python pro': []}
    file_storage = FileStorage(data)
    app = App(file_storage)

    app.remove_student()
    assert app.file_storage.data == data

    out, _ = capfd.readouterr()
    assert "Course: " in out
    assert "Enter student name to remove: " in out
    assert "Student John Doe not found in Course ." in out

    app.remove_student()
    assert app.file_storage.data == data

    out, _ = capfd.readouterr()
    assert "Course: " in out
    assert "Enter student name to remove: " in out
    assert "Student Jane Smith not found in Course ." in out

    app.remove_student()
    assert app.file_storage.data == {'Python basic': ['John Smith'], 'Python pro': []}

    out, _ = capfd.readouterr()
    assert "Course: " in out
    assert "Enter student name to remove: " in out
    assert "Student John Smith removed from Course ." in out
