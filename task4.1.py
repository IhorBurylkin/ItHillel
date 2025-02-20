list_1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for i in range(len(list_1) - 1, 0, -1):
    if list_1[i] == 0:
        list_1.pop(i)
        list_1.append(0)

print(list_1)

# i = 0
# len_list = len(list_1)

# while i < len_list:
#     if list_1[i] == 0:
#         list_1.pop(i)
#         list_1.append(0)
#         len_list -= 1
#     else:
#         i += 1

# print(list_1)