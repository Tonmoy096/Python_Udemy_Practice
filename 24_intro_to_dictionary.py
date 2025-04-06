# python dictionary


# A dictionary is a collection of key-value pairs.
# Each key is unique and is used to access its corresponding value.
# Dictionaries are mutable, meaning you can change their contents after creation.
# They are unordered collections, meaning the order of items is not guaranteed.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Each key-value pair is separated by a colon (:), and pairs are separated by commas (,).

student = {
    "name": "John",
    "age": "25",
    "Grade": "A",
    "City": "Dhaka"
}

print(student)
print(type(student))
print(len(student))

print(student["name"])
print(student["age"])
print(student["Grade"])
print(student["City"])
print(student.get("name"))


# modifying dictionary

student["Grade"] = "B+"

print(student)

print(student["Grade"])

print(student.keys())
print(student.values())
print(student.items())
