# while loops

count = 0

while count < 5:
    print("count:", count)
    count += 1


num = 10

while num > 0:
    print(num)
    num -= 2

password = ""

while password != "secret":  # "Keep looping as long as the password is NOT 'secret'"
    password = input('Enter the password:')

print("Welcome!")

n = 1
while True:
    print(n)
    n += 1
    if n > 5:
        break
