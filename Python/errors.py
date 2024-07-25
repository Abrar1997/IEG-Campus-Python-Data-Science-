#x = 11

# x = 10
# if (x % 2 == 0):
# print("Even Number")

#if (x % 2 == 0):
 #   print(f"Given Number is {x}")
#print("Even Number")

try:
    principle = int(input("Principle: "))
except ValueError:
    print("Principle amount must be an integer")
except Exception as e:
    print("Something went wrong:", e)
else:
    # The code inside the else block gets executed
    # only when there is no error
    print("All is well")
finally:
    print("Thank you")

principle = int(input("Principle:"))
period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * period * rate) / 100
print("Interest Amount: ", interest)