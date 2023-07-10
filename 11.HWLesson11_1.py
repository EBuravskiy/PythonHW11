def factorial(n):
    result = 0
    if n == 0:
        result = n
        list1.append(result)
        return n
    elif n == 1:
        result = n
        list1.append(result)
        return n
    result = n*(factorial(n-1))
    list1.append(result)
    return result


number = float(
    input("Enter a natural integer whose factorial you want to calculate: "))
list1 = list()
if (number < 0):
    print("Error! A negative number has been entered.")
elif (number % 1 > 0):
    print("Error! Not an integer entered.")
else:
    number = int(number)
    print(f"The factorial of {number} is {factorial(number)}")
    list1.reverse()
    print("The resulting list of calculations:")
    print(list1)
