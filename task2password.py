
import random
import string

# Prompt the user to enter desired password length
length = int(input("Enter the desired password length: "))

# All possible characters (letters + digits + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password
print("Generated Password:", password)
