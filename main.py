class  Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"

class Student(Human):
    def __init__(self, name, surname, age, sex, nationality):
        super().__init__(name, surname, age)
        self.sex = sex
        self.nationality = nationality
    def __str__(self):
        return f"{super().__str__()}, {self.gender}, {self.citizenship}"


class Group:
    def __init__(self):
        self.group_list = []

    def add_to_group(self, student):
        self.group_list.append(student)

    def remove_from_group(self, student):
        self.group_list.remove(student)

    def find_student(self, surname):
        for student in self.group_list:
            if student.surname == surname:
                return student

student_1 = Student("Marie", "Curie", 20, "female", "Poland")
student_2 = Student("Tom", "Cruise", 60, "male", "USA")
student_3 = Student("Mary", "Ivanova", 30, "female", "Italy")



group_1 = Group()
group_1.add_to_group(student_1)
group_1.add_to_group(student_2)
group_1.add_to_group(student_3)


group_1.remove_from_group(student_3)
print(group_1)
group_1.find_student("Cruise")
