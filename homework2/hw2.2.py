num1=float(input("Enter first number:  "))
operator=str(input("""Arithmetic operation 
        (+ - * /):   """))
print()
num2=float(input("Enter second number:  "))
print()

def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mult(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

print("Result:")
if operator=="+":
    print(f"{num1} + {num2} =", round(add(num1,num2),3))
elif operator=="-":
    print(f"{num1} - {num2} =",round(sub(num1,num2),3))
elif operator=="*":
    print(f"{num1} x {num2} =",round(mult(num1,num2),3))
elif operator=="/":
    print(f"{num1} : {num2} =",round(div(num1,num2),3))
else:
    print("choose '+', '-', '*' or '/' operator ")
print()