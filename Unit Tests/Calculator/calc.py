def main():
    a = float(input("Enter Number 1: "))
    b = float(input("Enter Number 2: "))
    op = input("Enter Operation: ")

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        raise ValueError("Invalid Operation")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    if b == 0:
        raise ValueError("Can't divide by 0")
    else:
        return a / b

if __name__ == "__main__":
    main()