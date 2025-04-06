# For loops

for num in range(5):
    print(num)


fruits = ["apple", "banana", "cherry", "Nothing"]
for fruit in fruits:
    print(fruit)


for index, fruit in enumerate(fruits):
    print(index, fruit)
    print(f"Index: {index}, Fruit: {fruit}")

for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end="\t")
    print()
