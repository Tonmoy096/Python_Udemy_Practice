# chr and ord

# chr() function: Converts an integer to its corresponding Unicode character.
# ord() function: Converts a Unicode character to its corresponding integer value.

num = 65
print(chr(num))  # asci value of 65 is A
print(ord("A"))  # ascii value of A is 65


# string Formating

str1 = "Hello my name is {First_name}{Last_name}".format(
    First_name="Tonmoy", Last_name="Sing")
print(str1)
