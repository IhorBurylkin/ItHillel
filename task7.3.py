def second_index(text: str, some_str: str): 
  first_i = text.find(some_str)
  if first_i == -1:
    return None
  
  second_i = text.find(some_str, first_i + 1)
  return second_i if second_i != -1 else None

second_index("hi", "h")