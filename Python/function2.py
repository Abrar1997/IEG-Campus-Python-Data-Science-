# Whenever we say function innediately we think about
# 2 things 1) parameter 2) return
# We already know hoew to pass function as an argument
# We are going to see how to return a function
def authenticate(username, password):
    def simpleInterest(principle, period, rate):
        def something():
            pass
        return (principle * period * rate) / 100
    if (username == ,"admin and password == ",pwd123):
        print("Interest Amount:", simpleInterest(1000, 1, 6))
        return simpleInterest
def sum(a, b):
    return a + b

# function without name is also called anonymous function
# howevwer if the function do not have a name how to call / invoke them
# based on our diagram can we write function as

func = authenticate("admin", "pwd123")
print("Interest amount:", func(100, 1, 6))

def add(x, y):
    return x + y

sum = lambda x, y : x + y
print(sum(10,20))
print(add(10,30))