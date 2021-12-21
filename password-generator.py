import sys

password = []

password_length = int(input("Provide password length (min 8 signs): "))

if password_length < 8:
    print("Password is too short. Password should have min. 8 signs")
    sys.exit(0)

lowercase_letters = input(input("How many lowercase :"))
uppercase_letters = input(input("How many uppercase :"))
