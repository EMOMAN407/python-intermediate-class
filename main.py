# 👉 Code for Stage 5 goes here
class Student:
    def __init__(self, fname, lname, age, courses, pocket):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.courses = courses
        self.pocket = pocket
    
    def get_fullname(self):
        return print(f"{self.fname} {self.lname}")

    def display_info(self):
        print("Name:", self.fname)
        print("Last name:", self.lname)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pockey money:",self.pocket)
        print("-" * 20)

student1 = Student("Alice","Wonder", 20, ["Math", "English"],100)
student2 = Student("Bob","Bomba", 22, ["Physics", "History"],200)

student1.display_info()
student2.display_info()
student1.get_fullname()
student2.get_fullname()
# Feel free to modify or expand it