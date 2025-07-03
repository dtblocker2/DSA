my_list = [1, 2, 3, 1, 2, 4, 7,6,5]
unique_list = []
[unique_list.append(x) for x in my_list if x not in unique_list]
print(unique_list)
