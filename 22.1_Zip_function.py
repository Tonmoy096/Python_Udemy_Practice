# Zip function

# The zip() function in Python is used to combine two or more iterables (like lists, tuples, etc.) into a single iterable of tuples. Each tuple contains elements from the input iterables at the same index. If the input iterables are of different lengths, zip() stops creating tuples when the shortest iterable is exhausted.

list1 = [1, 2, 3, 4, 5, 11]
list2 = [6, 7, 8, 9, 10, 100]

list3 = [11, 12, 13, 14, 15, 16]

# Using zip() to combine two lists
for a, b in zip(list1, list2):
    print(a, b)

length = len(list1)
print(length)

for i in range(length):
    print(list1[i], list2[i], list3[i])
