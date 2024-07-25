# Multiple inheritance
class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card Class")

class AtmCard(Card):
    def __init__(self):
        pass
    #def doSomething(self):
       # print("Inside AtmCard Class")

class CreditCard(Card):
    def __init__(self):
        pass
    #def doSomething(self):
        #print("Inside CreditCard Class")

class DebitCard(Card):
    def __init__(self):
        pass
    #def doSomething(self):
        #print("Inside DebitCard Class")

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        # print("Inside BankCard Class")
        super().doSomething()

# We have created 5 Classes
# And in All 5 classes we have doSomething method
# and it is implemented (got code inside which is "print")

# Let us create instance of the last card
bankCard = BankCard()
bankCard.doSomething()
# you will see "Inside BankCard Class"

# now remove the print statement from bankcard.dosomething
# this time you will see "Inside AtmCard Class" (which is the first inherited class)
print(BankCard.__mro__)

class Student:
    pass
    #def __str__(self):
       # return "Student"

class Alumni(Student):
    pass
    # def __str__(self):
        # return "Alumni"

alumni = Alumni()
print(alumni)