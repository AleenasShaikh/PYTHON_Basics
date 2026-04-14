

def add(a, b):
    return print(a + b)

def subtract(a, b):
    return print(a - b)

def multiply(a, b):
    return print(a * b)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

operation = {
    "+": add,
    "-": subtract,
    "*": multiply
}

op = input("Enter the operation (+, -, *): ")
if op in operation:
    operation[op](n1, n2)
else:    print("Invalid operation")