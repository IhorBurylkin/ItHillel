def popular_words (text, words):
    text_lower = text.lower()
    text_split = text_lower.split()
    result = {word: text_split.count(word) for word in words}

    return result    

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
print('OK')