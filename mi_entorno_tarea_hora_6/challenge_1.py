import random

def pass_gen(char_num):
    complex_words = [
        "Ardor", "Vigor", "Fable", "Lurid", "Mirth",
        "Nexus", "Quirk", "Raven", "Sable", "Thorn",
        "Vexed", "Witty", "Zesty", "Canny", "Eager",
        "Fjord", "Glint", "Haste", "Joust", "Keeny",
        "Lapse", "Mossy", "Noble", "Opine", "Plumb",
        "Rogue", "Slink", "Terse", "Unfed", "Wreak"
    ]

    german_words = [
        "Apfel", "Blume", "Fisch", "Hausz", "Katze",
        "Licht", "Mondy", "Nacht", "Pferd", "Quale",
        "Reise", "Schaf", "Sturm", "Traum", "Vogel",
        "Welle", "Zweig", "Birne", "Glanz", "Heide",
        "Kraft", "Laune", "Musik", "Rinde", "Sonne"
    ]

    special_characters = [
        "!", "@", "#", "$", "%",
        "^", "&", "*", "(", ")",
        "_", "+", "=", "{", "}",
        "[", "]", "|", "\\", "~"
    ]

    random_complex_w = random.choice(complex_words)
    random_german = random.choice(german_words)
    random_special_character = random.choice(special_characters)

    if char_num == 6:  # todo lo que hace es matchear con el input y regresa una palabra alemana + un character espacial
        return random_german + random_special_character
    elif char_num == 7:
        return random_complex_w + random_special_character+random_special_character
    elif char_num == 8:
        return random_complex_w + random_special_character+random_special_character+random_special_character
    elif char_num == 9:
        return random_complex_w + random_special_character+random_special_character+random_special_character+random_special_character
    elif char_num == 10:
        return random_complex_w + random_german
    elif char_num == 11:
        return random_complex_w + random_german+random_special_character
    elif char_num == 12:
        return random_complex_w + random_german+random_special_character
    elif char_num == 13:
        return random_complex_w + random_german+random_special_character+random_special_character+random_special_character
    elif char_num == 14:
        return random_complex_w + random_german+random_special_character+random_special_character+random_special_character+random_special_character
    elif char_num == 15:
        return random_complex_w + random_german+random_german
    elif char_num == 16:
        return random_complex_w + random_german+random_complex_w+random_special_character
    elif char_num == 17:
        return random_complex_w + random_german+random_complex_w+random_special_character+random_special_character
    elif char_num == 18:
        return random_complex_w + random_german+random_complex_w+random_special_character+random_special_character+random_special_character
    elif char_num == 19:
        return random_complex_w + random_german+random_complex_w+random_special_character+random_special_character+random_special_character+random_special_character
    elif char_num == 20:
        return random_complex_w+random_german+random_complex_w+random_special_character+random_special_character+random_special_character+random_special_character+random_special_character
    else:
        return "lenght not   valid  / / pls Try again /007"   

print(pass_gen(20))


