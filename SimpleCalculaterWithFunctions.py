def addition(numbers):
    print(numbers[0] + numbers[1])

def substraction(numbers):
    print(numbers[0] - numbers[1])

def multiply(numbers):
    print(numbers[0] * numbers[1])

def divide(numbers):
    print(numbers[0] / numbers[1])
    
while True:        

    operator = input("Enter Operator: ")

    if operator not in ['+', '-', '*', '/']:
        print("Invalid Operator")

    else:
        numbers = list(map(int, input("Enter two numbers: ").split()))

        if (operator == '+'):
            addition(numbers)

        elif (operator == "-"):
            substraction(numbers)
        
        elif (operator == "*"):
            multiply(numbers)

        elif (operator == "/"):
            divide(numbers)