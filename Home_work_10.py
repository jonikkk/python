import os
import json


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
        self.file_storage = file_storage

    def add_course(self):
        name = input("Enter course name: ")
        self.file_storage.data[name] = "Course"
        print(f"Course '{name}' added.")

    def show_courses(self):
        print("List of courses:")
        for course in self.file_storage.data:
            print(course)

    def run(self):
        while True:
            print("1. Add course")
            print("2. Show courses")
            print("3. Exit")
            choice = input("Select an option:")
            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.show_courses()
            elif choice == "3":
                self.file_storage.save_to_file(file_path)
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
