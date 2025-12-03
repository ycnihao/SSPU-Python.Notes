O# 1. 创建学生基类
class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def do_homework(self):
        print("学生做作业")


# 2. 派生类：小学生
class Pupil(Student):
    def __init__(self, name, number, is_young_pioneer):
        super().__init__(name, number)
        self.is_young_pioneer = is_young_pioneer

    # 3. 重写方法
    def do_homework(self):
        print("学生做作业")
        print("小学生做的是算术")


# 2. 派生类：大学生
class CollegeStudent(Student):
    def __init__(self, name, number, major, class_name):
        super().__init__(name, number)
        self.major = major
        self.class_name = class_name

    # 4. 重写方法
    def do_homework(self):
        print("学生做作业")
        print("大学生做的是定积分")


# 5. 作业函数
def homework(student):
    student.do_homework()


# 6. 创建对象并调用
p = Pupil("小明", "001", True)
c = CollegeStudent("张华", "2021001", "计算机科学", "计科1班")

homework(p)
homework(c)