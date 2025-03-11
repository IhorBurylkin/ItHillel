def is_palindrome(text: str):
    without_punct = "".join(i for i in text if i.isalnum()).lower()
    if without_punct == without_punct[::-1]:
        return True
    else:
        return False

print(is_palindrome("A man, a plan, a canal: Panama"))