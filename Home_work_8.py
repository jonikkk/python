class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


class Storage:
    saved_list = []

    def add(self, word):
        return Storage.saved_list.append(word)

    def get(self, key=''):

        if len(key) == 0:
            Storage.saved_list.sort()
            if len(Storage.saved_list) > 5:
                Storage.saved_list.pop()
            return Storage.saved_list
        else:
            return [word for word in Storage.saved_list if word.startswith(key)]


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, new_student):
        self.students.append(new_student)

    def to_json(self):
        student_list = [student.info() for student in self.students]
        return {'name': self.name, 'students': student_list}


if __name__ == '__main__':
    student = Student('John', 'Doe')
    assert student.info() == {'first_name': 'John', 'last_name': 'Doe'}
    fruits_storage = Storage()
    assert fruits_storage.get('') == []
    assert fruits_storage.get('apple') == []
    fruits_storage.add('plum')
    fruits_storage.add('apple')
    fruits_storage.add('peach')
    fruits_storage.add('apricot')
    fruits_storage.add('pineapple')
    assert fruits_storage.get('') == ['apple', 'apricot', 'peach', 'pineapple', 'plum']
    assert fruits_storage.get('a') == ['apple', 'apricot']
    assert fruits_storage.get('p') == ['peach', 'pineapple', 'plum']
    assert fruits_storage.get('abc') == []
    fruits_storage.add('pear')
    assert fruits_storage.get('') == ['apple', 'apricot', 'peach', 'pear', 'pineapple']
    python_basic = Course('Python basic')
    python_basic.add_student(Student('Jane', 'Doe'))
    python_basic.to_json()
    assert python_basic.to_json() == {
        'name': 'Python basic',
        'students': [{'first_name': 'Jane', 'last_name': 'Doe'}],
    }

    python_basic.add_student(Student('John', 'Doe'))
    assert python_basic.to_json() == {
        'name': 'Python basic',
        'students': [
            {'first_name': 'Jane', 'last_name': 'Doe'},
            {'first_name': 'John', 'last_name': 'Doe'},
        ],
    }
