'''
principle = 1000
period = 1
rate = 6
simpleInterest = (principle * period * rate) / 100
print("Simple Interest:", simpleInterest)
'''
'''
def calculateSimpleInterest():
    simpleInterest = (principle * period * rate) / 100
    return simpleInterest

def calculateTotalAMountToBePrinted(principle, simpleInterest)
    return principle + simpleInterest

principle = 1000
period = 1
rate = 6
result = calculateSimpleInterest(principle, period, rate)
newresult = calculateTotalAMountToBePrinted(principle, result)

print("Simple Interest:", result)
print("Total amount to be paid", newresult)
'''

class Student:
    def __init__(self):
        print("Object is created")
    
    def attendClass(self):
        print("Object started attending the class")
    
    def doProject(self, projectname):
        print("Object started doing the project:", projectname)
    
    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam: {exam} and obtained the score {grade}"
    
    

zul = Student()
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 120"))