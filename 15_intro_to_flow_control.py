# flow control

# if, elif, else


x = 10

if x > 5:
    print("x is greater than 5")


y = 3

if y > 5:
    print("y is greater than 5")

elif y == 3:
    print("y is equal to 3")

else:
    print("y is smaller")


# for loop

for i in range(8):
    print(i)

numbers = [1, 2, 3, 4, 5]

for num in numbers:

    if num == 6:
        break

else:
    print("loop completed without break")
