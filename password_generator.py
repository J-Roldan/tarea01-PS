import random
import string

# Recibe el largo y un bool por cada elemento que deba contener la contraseña
# Ademas permite valores repetidos
# Incluye al menos un carácter de cada tipo permitido
def random_password(length, lowercase, uppercase, digits, punctuation):
    characters = ''

    # Include at least one character from each allowed category
    if lowercase:
        characters += random.choice(string.ascii_lowercase)
    if uppercase:
        characters += random.choice(string.ascii_uppercase)
    if digits:
        characters += random.choice(string.digits)
    if punctuation:
        characters += random.choice(string.punctuation)

    # Add additional characters to meet the desired length
    remaining_length = length - len(characters)
    if remaining_length > 0:
        allowed_characters = ''
        if lowercase:
            allowed_characters += string.ascii_lowercase
        if uppercase:
            allowed_characters += string.ascii_uppercase
        if digits:
            allowed_characters += string.digits
        if punctuation:
            allowed_characters += string.punctuation

        # Generate additional characters randomly
        additional_characters = ''.join(random.choices(allowed_characters, k=remaining_length))
        characters += additional_characters

    # Shuffle the characters to ensure randomness
    shuffled_characters = random.sample(characters, len(characters))

    # Convert the list of characters to a string
    password = ''.join(shuffled_characters)

    return password