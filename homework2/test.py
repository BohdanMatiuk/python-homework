num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


op = input("Enter the operation (+, -, *, /): ")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    return x / y
   
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = sub(num1, num2)
    elif operation == "*":
        result = multi(num1, num2)
    elif operation == "/":
        result = div(num1, num2)
    else:
        result = "Invalid"

    print(f"Result: {result}")