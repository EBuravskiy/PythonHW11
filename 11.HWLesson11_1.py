number = int(
    input("Enter a natural integer whose factorial you want to calculate: "))
list1 = list()
if (number < 0):
    print("Error! A negative number has been entered.")
elif (number % 1 > 0):
    print("Error! Not an integer entered.")
else:
    factorial = 1
    list1.append(factorial)
    for i in range(2, number + 1):
        factorial *= i
        list1.insert(0, factorial)
print(f"The factorial of {number} is {factorial}")
print("The resulting list of calculations:")
print(list1)
