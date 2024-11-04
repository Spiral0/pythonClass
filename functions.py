# Built-in Functions

y = max(34, 56, 70, 18)
print(y)

x = max(40, 67, 34, 25)
print(x)

z = pow(2, 3)
print("The result is",z)

# User-defined functions
def greeting():
    print("Hello there")

greeting() #Calling function

def multiply():
    a = 12
    b = 10
    print(a * b)

multiply()

#Parameter/Variable and Argument/Value
def add(x, y):
    print( x + y )

add(4, 5)
add(60, 70)

def employee(fullname, age, position, status):
    print(fullname, age, position, status)

employee("John Doe", "53", "CEO", "Married")
employee("Jane Anne", "23", "HR", "Single")
employee("Albert Hue", "38", "Clerk", "Married")
employee("Mary Doe", "43", "Receptionist", "Married")