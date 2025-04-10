# list comprehension


# List comprehension is a concise way to create lists in Python.

# Syntax of list comprehension
# [expression for item in list]
# The expression is evaluated for each item in the iterable, and if the condition is true, the item is included in the new list.

list1 = []
for i in range(1, 51):
    list1.append(i)
print(list1)

# for odd number we can use 1 instead of 0
list2 = [ind for ind in range(1, 51) if ind % 2 == 0]
print(list2)
print(type(list2))
