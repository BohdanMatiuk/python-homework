num1=float(input("Enter first number:  "))
operator=str(input("""Arithmetic operation 
        (+ - * /):   """))
print()
num2=float(input("Enter second number:  "))
print()

print("Result:")
if operator=="+":
    print(f"{num1} + {num2} =",round((num1+num2),3))
elif operator=="-":
    print(f"{num1} - {num2} =",round((num1-num2),3))
elif operator=="*":
    print(f"{num1} x {num2} =",round((num1*num2),3))
elif operator=="/":
    print(f"{num1} : {num2} =",round((num1/num2),3))
else:
    print("choose '+', '-', '*' or '/' operator ")
print()