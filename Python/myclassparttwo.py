class Student:
    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""
    
    def attendClass(self):
        print(f"{self.firstname} {self.lastname} Object started attending the class")
    
    def doProject(self, projectname):
        print(f"{self.firstname} {self.lastname} Object started doing the project:", projectname)
    
    def attendExam(self, exam):
        grade = "A"
        return f"""{self.firstname} {self.lastname} 
        Object has attended the exam: {exam} and obtained the score {grade}"""
    
    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("IC Number:", self.icnumber)
    
    

zul = Student("Ahmad","Zul", 980102121234)
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 120"))
zul.info()
zul.program = ["Python", "Data Science", "Machine Learning"]