import random

list_1 = []

for i in range(0, random.randint(3, 10)):
    list_1.append(random.randint(0, 100))

result = [list_1[0], list_1[2], list_1[-2]]    
print(result)