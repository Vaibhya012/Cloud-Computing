import copy

original_list = [[1, 2, 3], [4, 5, 6]]

shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

shallow_copy[0][0] = 99
print(original_list) #output [[99, 2, 3], [4, 5, 6]] SHALLOW COPIES SHARE NESTED OBJECTS.

deep_copy[0][0] = 101
print(original_list) #output [[99, 2, 3], [4, 5, 6]] DEEP COPIES CREATE NEW ONES.