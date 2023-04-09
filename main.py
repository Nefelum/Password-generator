import random
import string

def password_generator(length=8, num_passwords=1, use_digits=True, use_exclamation_mark=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_exclamation_mark:
        characters += '!'

    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(length))
        yield password

# Example usage
num_passwords = 9
length = 24

for pwd in password_generator(length, num_passwords):
    print(pwd)
