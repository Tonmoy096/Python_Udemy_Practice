# truthy and Falsy


value = 10

if value:
    print("value is truthly")
else:
    print("Value is falsy")


# 0, "", [], {}, None, set() are falsy values in python
# all other values are truthy values in python

string = "hello"

if string:
    print("string is truthly")

else:
    ("string is falsy")

my_list = [1, 2, 3, 4, 5]

if my_list:
    print("Lis is truthly")
else:
    ("List is falsy")

my_dict = {"key": "Value"}

if my_dict:
    print("Dictionary is truthly")
else:
    print("Dictionary is falsy")


x = 0
if x:
    print("x is truthly")
else:
    print("x is falsy")

'''These are values that evaluate to False in a Boolean context:

Falsy Value	Explanation
False	The Boolean value False
None	The null value
0	Integer zero
0.0	Float zero
'' or ""	Empty string
[]	Empty list
{}	Empty dictionary
set()	Empty set
()	Empty tuple'''
