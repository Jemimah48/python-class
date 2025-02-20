def jemimah():
    print("Hello this is my function")
jemimah()

def calculatetwonumbers():
    num=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    print(f"the sum of{num} and{num2} is:{num+num2}")
calculatetwonumbers()
jemimah()
jemimah()

# function with parameter

def product_number(num3,num4):
    return num3*num4
print(product_number(3,4))