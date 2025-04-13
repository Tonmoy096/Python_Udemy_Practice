# converting string into list

userInput = input('Enter a string:')
print(userInput)

list1 = userInput.split()
print(list1)


list2 = []

for i in range(1, 5):
    userinput = input("Enter string:" + str(i)+":")
    print(userinput)
    list2.append(userinput)
print(list2)
