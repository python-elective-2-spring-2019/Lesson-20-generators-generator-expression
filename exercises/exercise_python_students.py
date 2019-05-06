"""
    Based on the student.py file from last lessons (Lesson 19) 
    create a PythonStudents class that acts as a collection of students. 
    The class should implement the iterations functionality (iter() and next()) 
    and be able to return an iter object. 
    When iterated the pythod_students object should return the name of each student 
    in the list.
    
"""
class PythonStudents:
    def __init__(self):
        self.students = []
        self.num = 0 # initial value
    
    def __add__(self, student):
        self.students.append(student)

    def __iter__(self):
        return self

    def __next__(self):
        
        if len(self.students) > self.num:
            x = self.students[self.num]
            self.num += 1
            return x
        else:
            raise StopIteration




class Student:

    def __init__(self, name, cpr):
        self.__name = name
        self.__cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return f'Im Anna, im the daughter of {self.name} :)'

    def __len__(self):
        return 180

    def __str__(self):
        return self.name + ' '

    def __repr__(self):
        return self.name
 
