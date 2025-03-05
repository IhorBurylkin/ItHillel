def correct_sentence(text: str):
    formatted_text = text.capitalize()
    if not formatted_text.endswith("."):
        formatted_text += "."
    return formatted_text

correct_sentence("greetings, friends")