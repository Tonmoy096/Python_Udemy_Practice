# del and list method

fruits = ["apple", "banana", "orange", "grape", "melon"]

del fruits[2]
print(fruits)

del fruits

# print(fruits)
# This will raise an error because the variable 'fruits' has been deleted

numbers = [3, 1, 5, 6, 2, 9, 8, 7, 10, 11]

numbers.sort()
print(numbers)

numbers.append(4)
print(numbers)


count = numbers.count(6)
print(count)


numbers.reverse()
print(numbers)

numbers.remove(4)
print(numbers)

numbers.clear()
print(numbers)
