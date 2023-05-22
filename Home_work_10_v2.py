import os
import json


class Pagination:
    def __init__(self, data, items_per_page=3):
        self.data = data
        self.items_per_page = items_per_page
        self.total_pages = (len(data) + items_per_page - 1)
        self.current_page = 1

    def get_current_page_data(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        if isinstance(self.data, list):
            page_data = self.data[start_index:end_index]
        elif isinstance(self.data, dict):
            keys = list(self.data.keys())[start_index:end_index]
            page_data = {key: self.data[key] for key in keys}
        else:
            page_data = []
        return page_data

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1


class FileStorage:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def load_from_file(file_path):
        if os.path.exists(file_path) and os.stat(file_path).st_size != 0:
            with open(file_path, "r") as f:
                data = json.load(f)
        else:
            data = {}
        return FileStorage(data)

    def save_to_file(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.data, f)


class App:
    def __init__(self, file_storage):
        self.pagination = None
        self.file_storage = file_storage

    def add_course(self):
        name = input("Enter course name: ")
        self.file_storage.data[name] = []
        print(f"Course '{name}' added.")

    def add_student(self):
        course = input("Course ")
        name = input("Enter student name ")
        lastname = input("Enter student lastname ")
        self.file_storage.data[course] += ([name + " " + lastname])
        print(f"Student {name} {lastname} added to Course {course} ")

    def show_courses(self):
        data = self.file_storage.data
        self.pagination = Pagination(data)
        print("List of courses:")
        while True:
            print("Page:", self.pagination.current_page)
            page_data = self.pagination.get_current_page_data()
            for course, students in page_data.items():
                print(f"Course={course} Students={students}")

            print("1. Next page")
            print("2. Previous page")
            print("3. Stop")

            option = input("Enter your option (1-3): ")
            if option == "1":
                self.pagination.next_page()
            elif option == "2":
                self.pagination.previous_page()
            elif option == "3":
                self.pagination = None
                break
            else:
                print("Invalid option. Please try again.")

    def run(self):
        while True:
            print("1. Add course")
            print("2. Show courses")
            print("3. Add Student")
            print("4. Exit")
            choice = input("Select an option:")
            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.show_courses()
            elif choice == "4":
                self.file_storage.save_to_file(file_path)
                break
            elif choice == "3":
                self.add_student()
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
