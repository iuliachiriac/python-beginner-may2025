list_of_lists = [[10, 20], [40], [30, 56, 25], [23, 14], [33], [], [40, 22, 47, 39]]
# renaming inner_list to list will cause shadowing
for inner_list in list_of_lists:
    # instead of calculating the length of the list (i),
    # the `len` function can be used:
    # i = len(inner_list)

    i = 0
    for nr in inner_list:
        i = i + 1

    # `len` function can be used directly in comparison expression
    # if len(inner_list) >= 2:
    if i >= 2:
        print(inner_list)

# when the built-in name list is shadowed, operations like the ones below
# don't work any longer
print("list=", list)
numbers = list(range(10))
print(numbers)
