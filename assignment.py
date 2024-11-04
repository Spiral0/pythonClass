
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def modulus(x, y):
    return x % y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y


print("Select operation: ")

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")

            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

            elif choice == '5':
                print(f"The result is: {modulus(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter numerical values.")
    else:
        print("Invalid choice. Please select a valid option.")

    next_calculation = input("Do you want to perform another calculation? yes(y)/no(n): ")
    if next_calculation.lower() != 'y':
        break
