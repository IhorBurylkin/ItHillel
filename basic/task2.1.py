number = input("Enter your number: ")
print(f'''{int(number[0]) % 1000}
{int(number[1]) % 100}
{int(number[2]) % 10}
{int(number[3]) // 1}''')

#or

print(f"""{int(number[0])}
{int(number[1])}
{int(number[2])}
{int(number[3])}
""")