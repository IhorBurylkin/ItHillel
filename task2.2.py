number = input("Enter your number: ")
output_number = [int(number[0]) % 10000,
int(number[1]) % 1000,
int(number[2]) % 100,
int(number[3]) % 10,
int(number[4]) // 1]
print(output_number[4] * 10000 + output_number[3] * 1000 + output_number[2] * 100 + output_number[1] * 10 + output_number[0])

#or

print(f"""{int(number[4])}
{int(number[3])}
{int(number[2])}
{int(number[1])}
{int(number[0])}
""")