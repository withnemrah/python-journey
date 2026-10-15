num1=float(input("Enter first number? "))
num2=float(input("Enter second number?"))
operation=(input("Enter operation"))
if operation == "/":
    if num2==0:
       print("Undefined")
    else:
       print("Division:", num1/num2)
elif operation=="*":
    print("Multiplication:", num1*num2)
elif operation =="+":
    print("Addition:", num1+num2)
elif operation =="-":
    print("Subtraction:", num1-num2)
else:
    print("Invalid operation")
