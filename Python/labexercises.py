# Zul Code
strNumber = "50,30,15,50,45,15,20,40"
# 50, 30, 20
# 15, 45, 40
# 30, 50, 20
listStrNumber = strNumber.split(",")
listNumber = []
for i in listStrNumber:
    listNumber.append(int(i))
unique_numbers = []
for i in listNumber:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(unique_numbers)
for num_1 in unique_numbers:
    for num_2 in unique_numbers:
        num_3 = 100 - (num_1+num_2)
        condition1 = (num_1!=num_2)
        condition2 = (num_1!=num_3)
        condition3 = (num_2!=num_3)
        if (num_3 in unique_numbers) and condition1 and condition2 and condition3:
            print(num_1, num_2, num_3)
            break

# Hanafi Effect
input_string = strNumber
numbers = []
for num in input_string.split(','):
    if int(num) not in numbers:
        numbers.append(int(num))
results = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 100:
                combination = [numbers[i], numbers[j], numbers[k]]
                if combination not in results:
                    results.append(combination)
if results:
    for result in results:
        print(f"The three unique numbers = 100: {result[0]} + {result[1]} + {result[2]}")
else:
    print("There are no three unique numbers.")

# Fifa algorithm
strNumbers = strNumber 
listStrNumbers = strNumbers.split(",")
listNumbers = []
for strNumber in listStrNumbers:
    listNumbers.append(int(strNumber))
 
uniqueNumbers = []
for count in range(0, len(listNumbers)):
    if listNumbers[count] not in uniqueNumbers:
        uniqueNumbers.append(listNumbers[count])
print(uniqueNumbers)
 
index = 0
for outputvariable1 in uniqueNumbers[index:]:
    innerindex= index + 1
    for outputvariable2 in uniqueNumbers[innerindex:]:
        outputvariable3 = 100 - (outputvariable1 + outputvariable2)
        if outputvariable3 in uniqueNumbers[innerindex + 1:]:
            print(outputvariable1, outputvariable2, outputvariable3)
            break
        innerindex += 1
    index += 1
 