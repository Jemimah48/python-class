# oop stands for object oriented programing
# A class is a blueprint of an object
# an object is a instance of a class
class Student:
    # constructor
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        # member functin
    def display(self):
        print(f"student name is:{self.name} Age is:{self.age} Score is:{self.score}")
# INSTANCE OF THE CLASS (OBJECT)
myobj=Student("jemimah",23,"A")
myobj.display()
myobj2=Student("Abigael",15,"B")
myobj2.display()
myobj3=Student("shan",19,"C")
myobj3.display()
myobj4=Student("Corine",20,"A-")
myobj4.display()
myobj5=Student("Julie",13,"c")
myobj5.display()
myobj6=Student("Janice",23,"C")
myobj6.display()

