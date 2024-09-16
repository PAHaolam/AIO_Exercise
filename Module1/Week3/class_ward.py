from abc import ABC, abstractmethod
import numpy as np


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_age(self):
        return 2024 - self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__people = []

    def add_person(self, person):
        self.__people.append(person)

    def describe(self):
        print(f'Ward name: {self.__name}')
        for per in self.__people:
            per.describe()

    def count_doctor(self):
        return sum([per.__class__.__name__ == 'Doctor' for per in self.__people])

    def sort_age(self):
        self.__people.sort(key=lambda x: x.get_age())

    def compute_average(self):
        return np.mean([per._yob for per in self.__people if per.__class__.__name__ == 'Teacher'])
