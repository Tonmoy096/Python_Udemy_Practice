# Nested dictionary

# A nested dictionary is a dictionary that contains other dictionaries as its values.
# This allows you to create complex data structures that can represent more intricate relationships between data.

students = {
    "student1": {
        "name": "John",
        "age": 25,
        "grade": "A",
        "city": "Dhaka"
    },
    "student2": {
        "name": "Jane",
        "age": 22,
        "grade": "B",
        "city": "Chittagong"
    },
    "student3": {
        "name": "Doe",
        "age": 24,
        "grade": "C",
        "city": "Sylhet"
    }
}

print(students)

for k, v in students.items():
    print(k, v["age"], v["grade"])
