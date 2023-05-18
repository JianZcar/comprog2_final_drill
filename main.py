import pandas as pd
from tabulate import tabulate as tb


class Name:
    def __init__(self, first=None, last=None, middle=None):
        self.first = first if first is not None else input("First Name: ").strip()
        self.last = last if last is not None else input("Last Name: ").strip()
        self.middle = middle if middle is not None else input("Middle Name: ").strip()

    def full_name(self):
        return f"{self.first} {self.middle} {self.last}"

    def input_name(self):
        self.first = input("First Name: ")
        self.middle = input("Middle Name: ")
        self.last = input("Last Name: ")
        return self.full_name()


class Student:
    def __init__(self, name=Name, age=None, course=None, year_level=None):
        self.name = name if name is not None else Name()
        self.name = self.name.full_name() if isinstance(self.name, Name) else self.name
        self.age = age if age is not None else int(input("Age: "))
        self.course = course if course is not None else input("Course: ")
        self.year_level = year_level if year_level is not None else int(input("Year Level: "))

    def get_info(self):
        return [self.name, self.age, self.course, self.year_level]


def user_login() -> bool:
    user_info = [input("Username: "), input("Password: ")]
    admin_user = ["ComputerScience", "PSU88@"]
    if user_info == admin_user:
        print("Welcome to the admin panel.")
        return True
    else:
        print("Incorrect username or password.")
        user_login()


def student_records() -> pd.DataFrame:
    return pd.DataFrame(columns=["Name", "Age", "Course", "Year Level"])


def add_student(name=None, age=None, course=None, year_level=None, student_r=None) -> pd.DataFrame:
    if student_r is None:
        student_r = student_records()
    student_r.loc[len(student_r)] = Student(name=name, age=age, course=course, year_level=year_level).get_info()
    return student_r


def search_student(student_r=None) -> None:
    if student_r is None:
        student_r = student_records()
    search = input("Search: ").strip()
    if search in student_r.values:
        print(student_r.loc[student_r["Name"] == search])


def update_course(student_r=None) -> None:
    if student_r is None:
        student_r = student_records()
    search = input("Search: ")
    if search in student_r.values:
        student_r.loc[student_r["Name"] == search, "Course"] = input("Course: ").strip()
        print(student_r.loc[student_r["Name"] == search])
    else:
        print("No student found.")
        update_course(student_r)


def filter_students_by_course(student_r=None) -> None:
    if student_r is None:
        student_r = student_records()
    course = input("Course: ").strip()
    (lambda x: print(tb(x, headers="keys", tablefmt="psql")))(student_r.loc[student_r["Course"] == course])


def count_students(student_r=None) -> None:
    if student_r is None:
        student_r = student_records()
    total = student_r["Course"].value_counts()
    print(f"Total number of students: {total.sum()}")


def recur_count_students(student_r=None, index=0) -> None:
    if student_r is None:
        student_r = student_records()
    if index == len(student_r):
        return print(f"Total number of students: {index}")
    else:
        recur_count_students(student_r, index + 1)


def display_students(student_r=None) -> None:
    if student_r is None:
        student_r = student_records()
    print(tb(student_r, headers="keys", tablefmt="psql"))
    print("Name: ", student_r["Name"].values)


def menu() -> int:
    list_of_choices = ["Add Student",
                       "Search Student",
                       "Update Course",
                       "Filter Students by Course",
                       "Display Students",
                       "Count Students",
                       "Exit"]
    [print(f"{i + 1}. {list_of_choices[i]}") for i in range(len(list_of_choices))]
    print("\n")
    return int(input("Choice: ").strip())


def main() -> None:
    student_r = student_records()
    while True:
        match menu():
            case 1:
                student_r = add_student(student_r=student_r)
                print("Student added.")
                print("\n")
            case 2:
                search_student(student_r=student_r)
                print("\n")
            case 3:
                update_course(student_r=student_r)
                print("\n")
            case 4:
                filter_students_by_course(student_r=student_r)
                print("\n")
            case 5:
                display_students(student_r=student_r)
                print("\n")
            case 6:
                recur_count_students(student_r=student_r)
                print("\n")
            case 7:
                exit()
            case _:
                print("Invalid choice.")
                continue


if __name__ == '__main__':
    main()
    pass
