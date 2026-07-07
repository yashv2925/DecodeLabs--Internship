# ===========================
# Random password genrator
# DecodeLabs - Project 3
# ===========================
import random
import string

print("Welcome to Password Generator")

while True:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Please enter at least 4 characters.\n")
    else:
        break

characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)
print("Keep your password safe!")