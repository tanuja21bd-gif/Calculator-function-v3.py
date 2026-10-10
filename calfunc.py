def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

# Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user to choose the operation
print("Choose an operation:")
print("1. Addition")
print("2. Multiplication")
choice = int(input("Enter your choice (1 or 2): "))

# Call the respective function based on the choice
if choice == 1:
    result = addition(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
elif choice == 2:
    result = multiplication(num1, num2)
    print(f"The product of {num1} and {num2} is {result}")
else:
    print("Invalid choice! Please enter 1 or 2.")