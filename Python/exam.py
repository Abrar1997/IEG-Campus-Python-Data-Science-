"""
print("Menu")

print("1.Name and Message")

print("2.Name")

argument1 = int(input())

name = input("Enter the name\n")

def greet(argument1,argument2 = "Welcome to Python Programming"):
  print(f"Hello {name}, {argument2}")
    
if argument1 == 1:
  message = input("Enter the message\n")
  greet(name, message)
elif argument1 == 2:
  greet(name)
"""
"""
argument1 = int(input())

def daysInYear(argument1,argument2=False):
  print(f"{argument1} is {argument2}")

if argument1 % 4 == 0:
  a = "a leap year"
  daysInYear(argument1,a)
else:
  b = "not a leap year"
  daysInYear(argument1,b)
"""
"""
def GCF (n1,n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1

def LCM (n1,n2):
    return (n1*n2) / GCF(n1,n2)

def GCD (n1,n2):
    return (n1*n2) / LCM(n1,n2)

print("Enter two integers")
n1 = int(input())
n2 = int(input())

(gcd) = GCD(n1,n2)
lcm = LCM(n1,n2)

print(f"Greatest common divisor of {n1} and {n2} = {int(gcd)}")
print(f"Least common multiple of {n1} and {n2} = {int(lcm)}")
"""
"""
print("Select the operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
o = int(input("Enter the choice(1/2/3/4/5):\n"))
n1 = int(input("Enter the first number\n"))
n2 = int(input("Enter the second number\n"))

def addition(n1,n2):
    return (n1 + n2)

def subtraction(n1,n2):
    return (n1 - n2)

def multiplication(n1,n2):
    return (n1*n2)

def division(n1,n2):
    return (n1 / n2)

def modulus(n1,n2):
    return (n1 % n2)

a = addition(n1,n2)
b = subtraction(n1,n2)
c = multiplication(n1,n2)
d = division(n1,n2)
e = modulus(n1,n2)

if o == 1:
    print(f"{n1}+{n2}={a}")
elif o == 2:
    print(f"{n1}-{n2}={b}")
elif o == 3:
    print(f"{n1}*{n2}={c}")
elif o == 4:
    print(f"{n1}/{n2}={d}")
elif o == 5:
    print(f"{n1}%{n2}={e}")
else:
    print("error")
"""
"""
number_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, 65, 39, 221]

# Get user input
n = int(input("Enter size of list\n"))

# Check for invalid input
if n == 0:
    print("Invalid Input")
else:
    while n > 0:
        for i in number_list:
            print(i)
        n = n - 1
"""
"""
a = int(input())
b = int(input())
def multiply (argument1,argument2 = 10):
    y = argument1*argument2
    print(f"The result is {y}")

multiply(a)
multiply(a,b)
multiply(a,9)
"""
"""
a = str(input("Enter department name:\n"))
b = int(input("Enter the number od total students:\n"))
c = int(input("Enter the number of total faculties:\n"))

def multiVarFunc(a,b,c):
    print("Details:")
    print(f"Department:{a}")
    print(f"Total students:{b}")
    print(f"Total faculties:{c}")

multiVarFunc(a,b,c)
"""
"""
def average_length(filename):
    try:

        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            total = sum(len(word) for word in words)
            n_of_words = len(words)

            if n_of_words == 0:
                return 0
            average = total / n_of_words

            print(int(average))

    except Exception as e:
        print(f"This error because:{e}")

average_length('averageLength.txt')
"""
"""
from sklearn.datasets import load_iris

i = load_iris()

print(f"Iris Feature Names\n{i.feature_names}")
print(f"Iris Target Names\n{i.target_names}")
print(f"Iris Feature Matrix\n{i.data[:5]}")
print(f"Iris Target Vector\n{i.target[:5]}")
print("Type of Iris Feature Matrix")
print(f"class '{str(type(i.data)).split("'")[1]}'")
print("Type of Iris Target Vector\n")
"""
fruits = {"apple", "banana", "cherry"}
print(fruits[0])