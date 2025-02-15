number_1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
number_2 = float(input("Enter second number: "))

if operation == "+":
    output = number_1 + number_2
elif operation == "-":
    output = number_1 - number_2
elif operation == "*":
    output = number_1 * number_2
elif operation == "/" and number_2 != 0:
    output = number_1 / number_2
else:
    print("Error input! Please try again")

print(f"Result: {output}")