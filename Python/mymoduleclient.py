#First Method
"""import mymodule

print(mymodule.add(10,20))
print(mymodule.minus(20, 10))
print(mymodule.multiplication(20,10))
print(mymodule.divide(20, 10))"""

#Second Method
'''from mymodule import add, minus, multiplication, divide
print(add(10,20))
print(minus(20,10))
print(multiplication(20,10))
print(divide(20, 10))'''

#Third Method
from mymodule import *
print(add(10,20))
print(minus(20,10))
print(multiplication(20,10))
print(divide(20, 10))