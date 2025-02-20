num=float(input("Enter first number: "))
num1=float(input("Enter second number: "))
operator=input("Enter operator (+,-*,/)")
if operator=="+":
    result=num+num1
    print(f"The result of {num} {operator} {num1} is{result}")
elif operator=="-":
    result=num-num1
    print(f"The result of {num} {operator} {num1} is{result}")
elif operator=="*":
    result=num*num1
    print(f"The result of {num} {operator} {num1} is{result}")
elif operator=="/":
    if num1 != 0:
        result=num/num1
        print(f"The result of {num} {operator} {num1} is{result}")
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")



