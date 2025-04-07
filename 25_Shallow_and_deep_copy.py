# shallow and Deep copy

import copy

original_list = [1, 2, [3, 4]]

shallow_copy = copy.copy(original_list)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)

shallow_copy[0] = 5
shallow_copy[2][0] = 6

print("After modifying shallow copy:", shallow_copy)
print("original list:", original_list)


deep_copy = copy.deepcopy(original_list)
print("Deep Copy:", deep_copy)
deep_copy[0] = 7
deep_copy[2][0] = 8
print("After modifying deep copy:", deep_copy)
