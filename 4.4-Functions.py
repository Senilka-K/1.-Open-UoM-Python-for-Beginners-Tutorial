def greet(name):
    "Greet a person with name"
    print("Hello ",name)
    return
greet("Nimal")
greet("Kamal")
print("")

def greet(name, msg="Good morning!"):  
    print("Hello", name + ', ' + msg) 

greet("Monica")
print("")

def greet(*names):
    for name in names:
             print("Hello", name)

greet("Drew","Dave","Daniel","David")
print("")

def add(a, b):
    return a+5, b+5
print(add(3, 2))
print("")

def myfunction(number):
    return number
print(myfunction(100))
print("")

def factorial(number):
      if number <= 1: 
          return 1
      return number * factorial(number-1)

print(factorial(5))
print("")

def sqr(n):
    "Return the square of the numeric parameter n."
    return n ** 2
print (sqr(4))
print("")