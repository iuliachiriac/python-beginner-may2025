list_of_lists = [[10, 20], [40], [30, 56, 25], [23, 14], [33], [], [40, 22, 47, 39]]
# renaming inner_list to list will cause shadowing
for inner_list in list_of_lists:
    i = 0
    for nr in inner_list:
        i = i + 1
    if i >= 2:
        print(inner_list)

# when the built-in name list is shadowed, operations like the ones below
# don't work any longer
print("list=", list)
numbers = list(range(10))
print(numbers)
