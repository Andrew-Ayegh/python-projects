import random

from argon2 import PasswordHasher

# Dear User, this is a password generator that generates passsword based on your desired Word/Number pair and length


def generate_password(letters, num_sym):
    letters = list(letters)
    num_sym = list(num_sym)
    letters.extend(num_sym)
    password = letters
    random.shuffle(password)
    print("".join(password), "is your newly generated password")


letter = input("letters you'd like to see in this password for easy familiarity   ").strip()
num_sym = input("numbers/symbols you'd like to see in your password for better familiarity  ").strip()
generate_password(letter, num_sym)

