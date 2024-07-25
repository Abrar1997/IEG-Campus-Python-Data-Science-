"""
def resistor(a,b,c):
    color = {Black,Brown,Red,Orange,Yellow,Green,Blue,Violet,Grey,White}
    number = {0,1,2,3,4,5,6,7,8,9}

    for i in color:
        if (i == a) and (i == b):
            print 
"""
class Employee():
  def __init__(self, id, name, salary, department):
    self.id = id
    self.name = name
    self.salary = salary
    self.department = department

  def calculateSalary(self, number_of_hours):
    if number_of_hours > 50:
      Overtime = number_of_hours - 50
      total_salary = self.salary * (Overtime * (self.salary/50))
    else:
      total_salary = self.salary
    return total_salary

  def assignDepartment(self, c_department):
    self.department = c_department

  def __str__(self):
    return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

e1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
e2 = Employee("E7499", "JONES", 45000, "RESEARCH")
e3 = Employee("E7900", "MARTIN", 50000, "SALES")
e4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")

print(e1)
e2.assignDepartment("IT")
print(e2)
y = e3.calculateSalary()
print(y)
