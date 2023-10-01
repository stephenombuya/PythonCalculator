import math


print('This is a simple calculator')
print("============================")
def add():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    print("The sum of " + str(num1) + " and " + str(num2) + " =", num1 + num2)

def sub():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    print("The difference of " + str(num1) + " and " + str(num2) + " =", num1 - num2)

def mult():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    print("The product of " + str(num1) + " and " + str(num2) + " =", num1 * num2)

def div():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    if num2 == 0:
        print("Cannot divide by zero, enter a non-zero number")
    else:
        print("The division of " + str(num1) + " and " + str(num2) + " =", num1 / num2)

def sqr():
    num = float(input('Enter a number: '))
    if num == 0:
        print("The square of 0 is 0")
    else:
        print("The square of " + str(num) + " =", num * num)

def sqrt():
    num = float(input('Enter a number: '))
    if num < 0:
        print("Not a number")
    elif num == 0:
        print("The squareroot of 0 is 0")
    else:
        print("The squareroot of " + str(num) + " =", math.sqrt(num))

def cub():
    num = float(input('Enter a number: '))
    if num == 0:
        print("The cube of 0 is 0")
    else:
        print("The cube of " + str(num) + " =", num * num * num)

def cbrt():
    num = float(input('Enter a number: '))
    if num == 0:
        print("The cuberoot of 0 is 0")
    else:
        print("The cuberoot of " + str(num) + " =", math.cbrt(num))

def log():
    num = float(input('Enter a number: '))
    if num <= 0:
        print("Not a number!")
    else:
        print("The logarithm of " + str(num) + " =", math.log10(num))

def sin():
    num = float(input('Enter a number: '))
    print("The sine of " + str(num) + " =", math.sin(num))

def cos():
    num = float(input('Enter a number: '))
    print("The cosine of " + str(num) + " =", math.cos(num))

def tan():
    num = float(input('Enter a number: '))
    print("The tangent of " + str(num) + " =", math.tan(num))

def asin():
    num = float(input('Enter a number: '))
    print("The sine inverse of " + str(num) + " =", math.asin(num))

def acos():
    num = float(input('Enter a number: '))
    print("The cosine inverse of " + str(num) + " =", math.acos(num))

def atan():
    num = float(input('Enter a number: '))
    print("The tangent inverse of " + str(num) + " =", math.atan(num))

def pow():
    num = float(input('Enter a number: '))
    exp_num = float(input('Enter an exponent number: '))
    print("The power of " + str(num) + " to " + str(exp_num) + " =", math.pow(num, exp_num))

while True:

    print("Enter operation to perform: ")
    print("")
    print("1. ADD")
    print("2. SUB")
    print("3. MULT")
    print("4. DIV")
    print("5. SQR")
    print("6. SQRT")
    print("7. CUB")
    print("8. CBRT")
    print("9. LOG")
    print("10. SIN")
    print("11. COS")
    print("12. TAN")
    print("13. ASIN")
    print("14. ACOS")
    print("15. ATAN")
    print("16. POW")

    print("")

    operation = input()
    if operation == "1":
        add()
    elif operation == "2":
        sub()
    elif operation == "3":
        mult()
    elif operation == "4":
        div()
    elif operation == "5":
        sqr()
    elif operation == "6":
        sqrt()
    elif operation == "7":
        cub()
    elif operation == "8":
        cbrt()
    elif operation == "9":
        log()
    elif operation == "10":
        sin()
    elif operation == "11":
        cos()
    elif operation == "12":
        tan()
    elif operation == "13":
        asin()
    elif operation == "14":
        acos()
    elif operation == "15":
        atan()
    elif operation == "16":
        pow()
    else:
        print("Invalid operation, please try again!")

    another_operation = input("Do you want to perform another operation? (yes/no): ").lower()
    if another_operation != "yes":
        break


