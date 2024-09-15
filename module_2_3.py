
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_1 = 0
while my_list_1 < len(my_list):
    if my_list[my_list_1] < 0:
        break
    if my_list[my_list_1] == 0:
        my_list_1 += 1
        continue
    print(my_list[my_list_1])
    my_list_1 += 1


