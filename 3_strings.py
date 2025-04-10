# String

greeting = "Hello"
name = "Tonmoy"

message = greeting + "," + name + "!"

print(message)

sentence = "i am learning python programming language"

print("The length of the sentence is:", len(sentence))

print("The first five character of the sentence is:", sentence[:5])
print("The last five character of the sentence is:", sentence[-5:])

# common string functions
str1 = "Welcome to PYTHON programming language"
print(str1.lower())

print(str1.upper())
print(str1.title())  # every first letter of a word will be capitalized
# only the first letter of the string will be capitalized
print(str1.capitalize())

# Advance string functions

str2 = "Hello, I am learning Python programming language"
print(str2.find("b"))

# print(str2.index("b"))
# The Python isalpha() String function examines a string for alphabetical characters and returns True only if the string contains all alphabetical characters.
print(str2.isalpha())
# must be digit all character then it will give true otherwise false
print(str2.isdigit())
