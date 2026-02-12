import random
import string

captcha = ''.join(random.choices(
    string.ascii_letters + string.digits,
    k=6
))

print("CAPTCHA:", captcha)

user_input = input("Retype the CAPTCHA: ")

if user_input == captcha:
    print("CAPTCHA verified successfully!")
else:
    print("Incorrect CAPTCHA. Try again.")