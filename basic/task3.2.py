list_1 = [12, 3, 4, 10]
list_2 = [1]
list_3 = []
list_4 = [12, 3, 4, 10, 8]

all_list = [list_1, list_2, list_3, list_4]

choice = int(input("Select list from 1 to 4: "))

if 1 <= choice <= 4:
    cur_list = all_list[choice - 1]
    if len(cur_list) > 1:
        last_number = cur_list.pop()
        cur_list.insert(0, last_number)
        print(cur_list)
    else:
        print("List is empty or has one element")
else:
    print("Enter correct number and try again")