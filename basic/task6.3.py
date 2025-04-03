digit = int(input("Enter your number: "))
iteration = 0

while digit >= 9:
    result = 1
    for num in str(digit):
        result *= int(num)
    digit = result
    iteration += 1

print(f"Result: {digit}, iterations: {iteration}")