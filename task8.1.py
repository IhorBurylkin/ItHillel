def add_one(some_list: list):
    digit = "".join(str(i) for i in some_list)
    return [int(i) for i in str(int(digit) + 1)]

print(add_one([9, 9, 9]))