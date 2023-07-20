def calculate(n):
    result = factorial(n)
    factorial_list.clear()
    result = factorial(result)


def factorial(n):
    result = 0
    if n == 0:
        result = n
        factorial_list.insert(0, result)
        return n
    elif n == 1:
        result = n
        factorial_list.insert(0, result)
        return n
    result = n*(factorial(n-1))
    factorial_list.insert(0, result)
    return result


number = float(
    input("Enter a natural integer whose you want to calculate: "))
factorial_list = list()
if (number < 0):
    print("Error! A negative number has been entered.")
elif (number % 1 > 0):
    print("Error! Not an integer entered.")
else:
    number = int(number)
    calculate(number)
    print(factorial_list)
