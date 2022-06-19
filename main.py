# Main file
import datetime


class Main:
    @staticmethod
    def date():
        now = datetime.datetime.now()
        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%y")
        date = f"{day}.{month}.{year}"
        return date

    @staticmethod
    def student():
        name = input("Student name ")
        surname = input("Student surname ")
        dob = input("Student birthdate ")
        student = f"{name} {surname} {dob}"
        st = student.capitalize()
        return st

    @staticmethod
    def subjects():
        subjects = input("Enter subject ")
        subject = subjects.capitalize()
        return subject

    @staticmethod
    def grade():
        grade: str = input("Grade of Student ")
        gd: float = float(grade)
        return gd

    @staticmethod
    def text():
        text = input("Enter text here ")
        txt = text.capitalize()
        return txt

    @staticmethod
    def teacher():
        name = input("Teacher name ")
        surname = input("Teacher surname ")
        fullname = f"{name} {surname}"
        ns = fullname.capitalize()
        return "Signed " + ns

    print(date(),
          "\n", student(),
          "\n", subjects(),
          "\n", grade(),
          "\n", text(),
          "\n", teacher())
