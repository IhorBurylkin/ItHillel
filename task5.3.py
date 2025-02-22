import string

input_string = input("Enter your string: ").split()

result = ("#" + "".join(["".join(word for word in split_word if word not in string.punctuation).capitalize() for split_word in input_string]))[:140]

print(result)