# Indexing and list slicing
# List slicing allows you to access a range of elements in a list.
# You can specify a start index, an end index, and a step value.
# The syntax is list[start:end:step].
# The start index is inclusive, while the end index is exclusive.
# The step value is optional and defaults to 1.
# It determines the increment between each index in the slice.

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(my_list)

print(my_list[0])  # Accessing the first element

print(my_list[1])  # Accessing the second element

print(my_list[-1])  # Accessing the last element


print(my_list[2:4])

print(my_list[::2])  # Accessing every second element

sliced_list = my_list[1:4]
print(sliced_list)
print(id(my_list))

sliced_list[1] = "graph"
print(sliced_list)
