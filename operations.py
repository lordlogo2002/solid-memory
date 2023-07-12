"""
    All operations get defined in here. Add them to the dict OPERATIONS with their
    representing math symbol as key so that the user can use it
"""
from random import randint

add = lambda a, b: a + b
sub = lambda a, b: a - b
div = lambda a, b: a / b
mul = lambda a, b: a * b
mud = lambda a, b: a % b
rnd = lambda a, b: randint(a, b)

OPERATIONS = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,
    "%": mud,
    "#": rnd
}

# used to show the operations to the user
operator_collection = ", ".join(OPERATIONS.keys())