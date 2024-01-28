while True:
    operator = input("enter operator: ")
    firstNumber = int(input("enter first number"))
    secondNumber = int(input("enter second number"))

    if (operator == '+'):
        print(firstNumber+secondNumber)
    elif (operator == "-"):
        print(firstNumber-secondNumber)
    elif (operator == "*"):
        print(firstNumber*secondNumber)
    elif (operator == "/"):
        print(firstNumber/secondNumber)
    else:
        print("invalid operator")