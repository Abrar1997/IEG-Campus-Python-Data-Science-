# Methods are nothing but functions inside the class
# Methods take atleast 1 parameter (self)
# This parameter is used by python to pass the instance
class calculator:
    # since this method take self as parameter (instance argument)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

mycalculator = calculator(10,20)
print(mycalculator.add())
print(mycalculator.subtract())

class Utility:

    def addition(x, y):
        return x + y
    
    def subtraction(x, y):
        return x - y
    
print(Utility.addition(100,300))
# however this can be easily done just using module in python
# no need to create a class
class Customer:
    # instance method
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    # class method
    def getFullname(firstname, lastname):
        return firstname + lastname
    # instance method
    def __str__(self):
        return Customer.getFullname(self.firstname, self.lastname)
    
myCustomer = Customer("John", "David")
print(myCustomer)