# Calculator Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division not possible"

'''
# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", sub(num1, num2))
print("Multiplication:", mul(num1, num2))
print("Division:", div(num1, num2))
'''