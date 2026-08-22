import json


class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0

        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"ID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Marks   : {self.marks}")
        print(f"Average : {self.average():.2f}")
        print("-" * 30)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["marks"]
        )


class StudentManagementSystem:

    def __init__(self):
        self.students = {}

    # ---------------- ADD ----------------

    def add_student(self):
        try:
            student_id = input("Enter student ID: ")

            if student_id in self.students:
                print("Student already exists.")
                return

            name = input("Enter student name: ")

            age = int(input("Enter age: "))

            if age <= 0:
                raise ValueError("Age must be positive.")

            marks = list(
                map(
                    float,
                    input("Enter marks separated by spaces: ").split()
                )
            )

            student = Student(
                student_id,
                name,
                age,
                marks
            )

            self.students[student_id] = student

            print("Student added successfully.")

        except ValueError as e:
            print("Invalid input:", e)

    # ---------------- DELETE ----------------

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")

        if student_id not in self.students:
            print("Student not found.")
            return

        del self.students[student_id]

        print("Student deleted successfully.")

    # ---------------- UPDATE ----------------

    def update_student(self):
        student_id = input("Enter student ID to update: ")

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        try:
            print("Leave input empty to keep the old value.")

            name = input(f"Enter name [{student.name}]: ")

            if name:
                student.name = name

            age = input(f"Enter age [{student.age}]: ")

            if age:
                age = int(age)

                if age <= 0:
                    raise ValueError("Age must be positive.")

                student.age = age

            marks = input(
                f"Enter marks [{student.marks}]: "
            )

            if marks:
                student.marks = list(
                    map(float, marks.split())
                )

            print("Student updated successfully.")

        except ValueError as e:
            print("Invalid input:", e)

    # ---------------- SEARCH ----------------

    def search_student(self):
        student_id = input("Enter student ID to search: ")

        student = self.students.get(student_id)

        if student is None:
            print("Student not found.")
            return

        student.display()

    # ---------------- DISPLAY ----------------

    def display_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n===== STUDENT LIST =====")

        for student in self.students.values():
            student.display()

    # ---------------- AVERAGE ----------------

    def calculate_average(self):
        student_id = input("Enter student ID: ")

        student = self.students.get(student_id)

        if student is None:
            print("Student not found.")
            return

        print(
            f"Average marks: {student.average():.2f}"
        )

    # ---------------- SAVE ----------------

    def save_data(self):
        try:
            data = []

            for student in self.students.values():
                data.append(student.to_dict())

            with open("students.json", "w") as file:
                json.dump(data, file, indent=4)

            print("Data saved successfully.")

        except IOError as e:
            print("Error saving data:", e)

    # ---------------- LOAD ----------------

    def load_data(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

            self.students = {}

            for student_data in data:
                student = Student.from_dict(student_data)

                self.students[student.student_id] = student

            print("Data loaded successfully.")

        except FileNotFoundError:
            print("No saved data found.")

        except json.JSONDecodeError:
            print("File contains invalid data.")

        except IOError as e:
            print("Error loading data:", e)

    # ---------------- MENU ----------------

    def menu(self):

        while True:

            print("\n========== STUDENT MANAGEMENT SYSTEM ==========")

            print("1. Add Student")
            print("2. Delete Student")
            print("3. Update Student")
            print("4. Search Student")
            print("5. Calculate Average")
            print("6. Display Students")
            print("7. Save Data")
            print("8. Load Data")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.delete_student()

            elif choice == "3":
                self.update_student()

            elif choice == "4":
                self.search_student()

            elif choice == "5":
                self.calculate_average()

            elif choice == "6":
                self.display_students()

            elif choice == "7":
                self.save_data()

            elif choice == "8":
                self.load_data()

            elif choice == "9":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please try again.")


# Create application
system = StudentManagementSystem()

# Load previously saved data
system.load_data()

# Start application
system.menu()