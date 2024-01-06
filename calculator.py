def main():
print("Welcome to our python calculator!")
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operation == '+':
print("Result: ", add(num1, num2))
elif operation == '-':
print("Result: ", subtract(num1, num2))
elif operation == '*':
print("Result: ", multiply(num1, num2))
elif operation == '/':
print("Result: ", divide(num1, num2))
else:
print("Oops! Invalid operation. Please try again!")

# Call the main function to start our calculator
main()
