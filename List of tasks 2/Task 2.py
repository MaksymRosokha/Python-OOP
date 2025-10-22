class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) >= 3 and name.isalpha():
            self._name = name
        else:
            print("Invalid name")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if len(surname) >= 3 and surname.isalpha():
            self._surname = surname
        else:
            print("Invalid surname")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 0 <= age <= 130:
            self._age = age
        else:
            print("Invalid age")

    def __str__(self):
        return f"{self._name} {self._surname} has {self._age} years old."


class Student(Person):
    def __init__(self, name, surname, age, major, grades = dict()):
        super().__init__(name, surname, age)
        self._major = major
        self._grades = grades

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        if isinstance(grades, dict):
            self._grades = grades
        else:
            print("Invalid surname")

    def add_grade(self, grade, subject):
        self._grades[subject] = grade

    def __str__(self):
        return f"{self._name} {self._surname} has {self._age} years old. {self._name} is a student."

class Employee(Person):
    def __init__(self, name, surname, age, position, skills):
        super().__init__(name, surname, age)
        self._position = position
        self._skills = skills

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, skills):
        self._skills = skills
