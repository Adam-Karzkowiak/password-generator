import sys
import random
import string

password = []
characters_left = -1


def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Number of characters out of range 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Characters left :", characters_left)


password_length = int(input("Provide password length (min 8 signs):"))

if password_length < 8:
    print("Password is too short. Password should have min. 8 signs")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("How many lowercase:"))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("How many uppercase:"))
update_characters_left(uppercase_letters)

special_characters = int(input("How many special characters:"))
update_characters_left(special_characters)

digits = int(input("How many digits:"))
update_characters_left(digits)

if characters_left > 0:
    print("Rest of characters will be filled with lowercase letters")
    lowercase_letters += characters_left

print()
print("Password length:", password_length)
print("Lowercase letters:", lowercase_letters)
print("Uppercase letter:", uppercase_letters)
print("Special characters:", special_characters)
print("Digits:", digits)

for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Password:", "".join(password))
