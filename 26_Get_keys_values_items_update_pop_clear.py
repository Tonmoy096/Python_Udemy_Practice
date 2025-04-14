my_dict = {
    "apple": 5,
    "banana": 10,
    "orange": 8
}

apple_quantity = my_dict.get("apple")
print("The quantity of the apple is:", apple_quantity)

del my_dict['apple']
print("After removing apple:", my_dict)

print("The quantity of the apple is:", my_dict.get("apple"))
print("The quantity of the banana is:", my_dict.get("banana"))

my_dict.update({"kiwi": 100})
print(my_dict)
