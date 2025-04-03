import string

def first_word(text: str) -> str:
    punctuation_to_remove = string.punctuation.replace("'", "")
    new_text = (''.join(' ' if char in punctuation_to_remove else char for char in text))
    result = new_text.split()
    return result[0]

assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word(".., and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print('OK')