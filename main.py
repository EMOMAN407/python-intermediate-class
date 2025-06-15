# 👉 Code for Stage 5 goes here
class Student:
    def __init__(self, name, lastn, age, courses, pocket):
        self.name = name
        self.lastn = lastn
        self.age = age
        self.courses = courses
        self.pocket = pocket

    def display_info(self):
        print("Name:", self.name)
        print("Last name:", self.lastn)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pockey money:",self.pocket)
        print("-" * 20)

student1 = Student("Alice","Wonder", 20, ["Math", "English"],100)
student2 = Student("Bob","Bomba", 22, ["Physics", "History"],200)

student1.display_info()
student2.display_info()
# Feel free to modify or expand it