# making a simple calculator

# using the eval function to evaluate the expression

val1 = eval(input("Please enter a number:"))

val2 = eval(input("Please enter another number:"))

operator = input("Please enter the operator (+, -, *, /):")

if operator == "+":
    print(val1 + val2)
elif operator == "-":
    print(val1 - val2)
elif operator == "*":
    print(val1 * val2)
elif operator == "/":
    print(val1/val2)
else:
    print("Please enter a valid operator")
