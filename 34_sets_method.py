# sets method

my_set = {1, 2, 3, 4, 5, 6}
my_set.add(7)
print("Here is the updated set:", my_set)
my_set.add(1)
print("Here is the updated set:", my_set)

my_set.remove(3)
print("After removing 3 my updated set is :", my_set)
my_set.discard(2)
print("After removing 2 my updated set is :", my_set)

my_set.update([8, 9, 10])  # i can use both curly bracees and square braces
print("After updating my set is :", my_set)


pop_element = my_set.pop()
print("Here is the popped element:", pop_element, type(pop_element))
