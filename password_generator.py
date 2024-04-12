from random import sample

# Recibe el largo y un bool por cada elemento que deba contener la contraseña
# Ademas permite valores repetidos
def random_password(large, its_lower, its_upper, its_numbers, its_symbols):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()
    numbers = "0123456789"
    symbols = "~`! @#$%^&*()_-+={[}]|:\\;\"'<,>./?"
    all_characters = ""
    if(its_lower):
        all_characters += lower_case
    if (its_upper):
        all_characters += upper_case
    if(its_numbers):
        all_characters += numbers
    if(its_symbols):
        all_characters += symbols
    all_characters += all_characters
    while(len(all_characters) < large):
        all_characters += all_characters
    return "".join(sample(all_characters, large))
