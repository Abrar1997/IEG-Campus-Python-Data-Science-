# Is - A Relationship
# Alumni is a Student
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

# ALumni extends Student class
class Alumni(Student):

    def __init__(self, firstname, lastname, alumninumber):
        # Student.__init__(self, firstname, lastname)
        # calling the __init__ method statically
        # self.student = Student()
        # To create the parent object inside the child object
        # you can use super class
        # which will return the object of parent class
        super().__init__(firstname, lastname)
        self.alumninumber = alumninumber
    
    def __str__(self):
        return f"First Name: {self.firstname} \
            \nLast Name: {self.lastname} \
            \nIC Number:{self.icnumber} \
            \nAlumni Number: {self.alumninumber}"
    
# we have create and object of Alumni class
alumni = Alumni("Parker","Peter", 97409)
#alumni = Alumni()
print(alumni)

