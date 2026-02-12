import random
import string

length = int(input("Enter password length (8-12): "))

upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special = random.choice("!@#$%^&*")

remaining = ''.join(random.choices(
    string.ascii_letters + string.digits + "!@#$%^&*",
    k=length-4
))

password_list = list(upper + lower + digit + special + remaining)
random.shuffle(password_list)

password = ''.join(password_list)

print("Generated Password:", password)
