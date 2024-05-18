

from random import choice

lst = ["Circle", "Ellipse", "Square"]

def return_random_target() -> str:
    result = choice(lst)
    return result