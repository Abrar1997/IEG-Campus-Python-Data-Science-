# Only in python the function cn access the variable
# declared in the main context
x = 10

def sayX():
    x = 0
    print(x) # usually x is initialized and then only used
    # in this case "function can see x"

sayX()

def modifyX():
    x = 20
    # whenever you modify the varibale which is in the global context
    # the variable is initialized locally
    # in this case x automatically become local variable
    print(x)

modifyX()
print(x)

