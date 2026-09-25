operator=input("enter your operator (- , * , / , +)")
num1=float(input("enter your first number"))
num2=float(input("enter your second number"))
if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    result=num1/num2
    print(result)
