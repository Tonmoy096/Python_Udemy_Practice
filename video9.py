#Array

my_array=[1,2,3,4,5,6,7,8,9,]
print(my_array)

print("first elements of the array:", my_array[0])
print("Last element of the array:", my_array[-1])

print("Slicing the array:", my_array[1:8])

my_array[5]=10
print("Modified array:", my_array)

print("Array length:", len(my_array))

my_array.append(11)
print("Updated array:", my_array)

my_array.remove(4)
print("Updated array after removing:", my_array)

my_array.sort()
print(my_array)

my_array.reverse()
print(my_array)

print("Is 10 in array?:", 10 in my_array)