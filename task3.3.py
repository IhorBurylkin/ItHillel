list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3, 4, 5]
list_4 = [1]
list_5 = []

all_list = [list_1, list_2, list_3, list_4, list_5]

choice = int(input("Select list from 1 to 5: "))

if 1 <= choice <= 5:
    cur_list = all_list[choice - 1]
    count_split_list = (len(cur_list) + 1) // 2
    first_half = cur_list[:count_split_list]
    second_half = cur_list[count_split_list:]
    print(first_half, second_half)  
else:
    print("Enter correct number and try again")