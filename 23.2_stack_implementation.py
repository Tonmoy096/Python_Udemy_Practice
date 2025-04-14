# implementations


# stack is a linear data structure that follows the LIFO (Last In First Out) principle.
# The last element added to the stack is the first one to be removed.

# It can be implemented using a list or a linked list.

list1 = []
while True:
    oprInput = int(input('''
    1. Push Element
    2. Pop Element    
    3. Peek Element
    4. Display Stack
    5. Exit
    '''))
    if oprInput == 1:
        userInput = input("Enter the value:")
        list1.append(userInput)
        print(list1)
    if oprInput == 2:
        if len(list1) == 0:
            print("Stack is empty")
        else:
            popElement = list1.pop()
            print("Pop element:", popElement)
            print(list1)
    if oprInput == 3:
        if len(list1) == 0:
            print("Stack is empty")
        else:
            peekElement = list1[-1]
            print("Peek element:", peekElement)
            print(list1)
    if oprInput == 4:
        if len(list1) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", list1)
    if oprInput == 5:
        print("Exiting...")
        break
