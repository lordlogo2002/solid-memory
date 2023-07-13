from typing import Any
from colorama import Fore

class MetaColor(type):
    """
    This Meta Class controls wether the console output is colored or not.
    This is controlled by the `MetaColor.USE_COLOR` flag.
    If color output is activated the class attributes of the class will
    return their value otherwise an empty string.
    if the class attr is all upper case or starts with a "_" it will
    always return its value neither the state of the USE_COLOR flag
    """
    USE_COLOR = True

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    def __getattribute__(cls, name:str):
        if name.isupper() or name.startswith("_") or cls.USE_COLOR:
            return type.__getattribute__(cls, name)
        return ""

class Color(metaclass=MetaColor):
    title = Fore.GREEN
    normal_text = Fore.CYAN
    info_text = Fore.LIGHTMAGENTA_EX
    prompt = Fore.MAGENTA
    user_input = Fore.YELLOW
    error_message = Fore.RED
    reset = Fore.RESET

color_keys = {
    "%t": Color.title,
    "%n": Color.normal_text,
    "%i": Color.info_text,
    "%ui": Color.user_input,
    "%e": Color.error_message
}

reset_color = lambda: print(Color.reset, end="\r") # simplified way to clear colors without crating a new line

def parse_colors(text:str) -> str:
    """
        go trough the text and add color codes
        colors can be changed in colored.Color:
         - %t for title
         - %n for normal_text
         - %i for info_text
         - %ui for user_input
         - %e for error_message
    """
    for color_key, color_code in color_keys.items():
        text = text.replace(color_key, color_code)

    return text

def colored_print(text:str) -> None:
    """
        procedure to parse color codes, print them and reset colors afterwards
        color codes are listed in `parse_colors`
    """
    text = parse_colors(text)
    print(text)
    reset_color()

error_message = colored_print # for easier readability in code

def colored_input(prompt:str) -> str:
    """
        procedure to parse color codes, asks for input with the given prompt and resets the colors after input
        color codes are listed in `parse_colors`
    """
    prompt = parse_colors(prompt)
    value = input(Color.prompt+prompt+Color.user_input)
    reset_color()
    return value

def run_colored(func):
    """ run the function an reset colors afterwards, even if a exception is thrown """
    try:
        func()
    finally:
        reset_color()
