#!/usr/bin/env python


class SchoolMember(object):
    def __init__(self, name, age):
        self.name, self.age = name, age
        print("SchoolMember初始化成功， {}".format(self.name))

    def tell(self):
        """告诉调用者你的信息"""
        print("Hi, i am {}, my age is {}".format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("老师初始化成功，{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("my salary is {}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print("学生创建成功 {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("{}'s mark is {}".format(self.name, self.mark))

if __name__ == "__main__":
    sam = Teacher("任老师", 18, 10000000)
    sam.tell()

    tom = Student('tom', 18, 90)
    tom.tell()