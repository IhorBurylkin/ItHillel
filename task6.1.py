import string

input_string = input("Enter a range of letters: ")

start_letter, end_letter = input_string.split("-")
start_letter =  string.ascii_letters.index(start_letter)
end_letter = string.ascii_letters.index(end_letter)
result = string.ascii_letters[start_letter:end_letter + 1]

print(f"Result: {result}")