# join sets


set1 = {1, 2, 77, 4, 5}
set2 = {6, 5, 7, 8, 9, 10}

joined_set = set1.union(set2)
print("Here is the joined set:", joined_set)

set1.update(set2)

print("The updated set1 is:", set1)
joined_set = set1 | set2

print(joined_set)
joined_set = set1 & set2
print(joined_set)
joined_set = set1 - set2
print(joined_set)
