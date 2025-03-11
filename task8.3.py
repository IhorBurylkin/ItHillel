def find_unique_value(some_list: list): 
    lst = {}
    for i in some_list:
      if i in lst:
         lst[i] += 1
      else:
         lst[i] = 1
    
    for key, num in lst.items():
      if num == 1:
        return key

print(find_unique_value([5, 5, 5, 2, 2, 0.5]))