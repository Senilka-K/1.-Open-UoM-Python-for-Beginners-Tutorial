def add(a,b):
    return a+b
    
def substract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("float division by zero")
        return "None"
        
def power(a,b):
    return a^b
    
def remainder(a,b):
    if b != 0:
        return a % b
    else:
        return "Error: Cannot find remainder with zero divisor"
        
def terminate():
    print("Done. Terminating")
    exit()

def reset():
    print("Resetting...")

def select_op(choice):
    if choice in {'+', '-', '*', '/', '^', '%'}:
        try:
            a = (input("Enter first number: "))
            print(a)
            a=float(a)
            b = (input("Enter second number: "))
            print(b)
            if b == '#':
                terminate()
            else:
                b=float(b)
        except ValueError:
            return
        
        
        if choice == '+':
            result = add(a, b)
        elif choice == '-':
            result = subtract(a, b)
        elif choice == '*':
            result = multiply(a, b)
        elif choice == '/':
            result = divide(a, b)
            if "float division by zero" in result:
                print(result)
                return
        elif choice == '^':
            result = power(a, b)
        elif choice == '%':
            result = remainder(a, b)

        print(f"{a} {choice} {b} = {result}")

    elif choice == '#':
        terminate()
    elif choice == '$':
        reset()
    else:
        print("Unrecognized operation")


while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()