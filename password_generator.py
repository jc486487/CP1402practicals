import random
length = int(input("Enter the required length of the password: "))

print("What is the minimum number of lower case alphabets to be included?")
lower = int(input(">"))

print("What is the minimum number of upper case alphabets to be included?")
upper = int(input(">"))

print("What is the minimum number of digits to be included in the program?")
numbers = int(input(">"))

print("Enter the characters should be included? eg.#$@")
charac = str(input(">"))

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYX0123456789"
all_charac = alpha + charac

password = ""
count_lower =0
count_upper = 0
count_digit = 0
count_special= 0
success = False



while not success:
    password=""
    while len(password)< length:
        password += random.choice(all_charac)

    for char in password:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if char in charac:
            count_special += 1

    if count_upper >= upper and count_lower>=lower and count_digit >= numbers and count_special>=1:
         success = True

print("Generated password: ", password)