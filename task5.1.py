import keyword, string

input_string = input("Enter name of var: ")

check_condition = [
    input_string != "",
    not input_string[0].isdigit(),
    not any(i.isupper() for i in input_string),
    not any(i.isspace() for i in input_string),
    not any(i in string.punctuation and i != "_" for i in input_string),
    input_string not in keyword.kwlist,
    input_string.count("_") <= 1
]

print(all(check_condition))